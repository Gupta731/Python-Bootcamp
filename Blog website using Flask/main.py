import html
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from functools import wraps
import smtplib
from sqlalchemy.orm import relationship
from forms import *
from flask_gravatar import Gravatar
import os


app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = 'myapp123'
Bootstrap(app)

MY_EMAIL = 'sourabhmahan@gmail.com'
PASSWORD = os.environ.get('PASSWORD')
TO_EMAIL = 'tiu.f2.cse@gmail.com'
YEAR = datetime.now().year

# Connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False,
                    base_url=None)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Admin only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)

    return decorated_function


# User table Parent
class User(UserMixin, db.Model):
    """Stores user data"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    # This will act like a List of PostTable objects attached to each User.
    # The "author" refers to the author property in the PostTable class.
    posts = relationship('PostTable', back_populates='author')
    comments = relationship('Comment', back_populates='comment_author')


# Posts table configurations child
class PostTable(db.Model):
    """Stores all the blog posts"""
    __tablename__ = 'post_table'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    author = relationship('User', back_populates='posts')
    img_url = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    comments = relationship('Comment', back_populates='parent_post')


# Comments table
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_author = relationship('User', back_populates='comments')
    post_id = db.Column(db.Integer, db.ForeignKey('post_table.id'))
    parent_post = relationship('PostTable', back_populates='comments')


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    """Home route shows all blog posts"""
    posts = PostTable.query.all()
    return render_template("index.html", all_posts=posts, current_year=YEAR)


@app.route('/register', methods=["GET", "POST"])
def register():
    """Route for new user registrations"""
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        if User.query.filter_by(email=register_form.email.data).first():
            flash('User already registered. Please Login', 'error')
            return redirect(url_for('login'))
        else:
            new_user = User(email=register_form.email.data,
                            password=generate_password_hash(register_form.password.data, method='pbkdf2:sha256',
                                                            salt_length=8),
                            name=register_form.name.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
    return render_template("register.html", form=register_form, current_year=YEAR)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Route for existing user login"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            flash('User not registered. Please register first.', 'error')
            return redirect(url_for('register'))
        else:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Incorrect Password. Try Again', 'error')
                return redirect(url_for('login'))
    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    """Logs out currently active user"""
    logout_user()
    return redirect(url_for('home'))


@app.route('/about')
def about_page():
    """Route for about page"""
    return render_template("about.html", current_year=YEAR)


@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    """Route for contact me page"""
    if request.method == 'POST':
        data = request.form
        send_mail(data['name'], data['email'], data['phone'], data['message'])
        return render_template("contact.html", current_year=YEAR, msg_sent=True)
    return render_template("contact.html", current_year=YEAR, msg_sent=False)


def send_mail(name, email, phone, message):
    """Sends email to webapp owner"""
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,
                            msg=f"From: Saurabh Gupta <{MY_EMAIL}>\n"
                                f"To: {TO_EMAIL}\n"
                                f"Subject: My Blogs message\n\n"
                                f"Name: {name}\n"
                                f"Email: {email}\n"
                                f"Phone: {phone}\n"
                                f"Message: {message}")
        print('Message sent')


@app.route('/post/<int:post_id>', methods=["GET", "POST"])
def get_post(post_id):
    """Route for viewing specific posts"""
    requested_post = PostTable.query.get(post_id)
    blog_comments = Comment.query.filter_by(post_id=post_id).all()
    comments_form = CommentsForm()
    if comments_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('You need to login or register to comment.')
            return redirect(url_for('login'))
        new_comment = Comment(text=comments_form.comment.data,
                              comment_author=current_user,
                              parent_post=requested_post)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('get_post', post_id=post_id))
    return render_template("post.html", post=requested_post, body=html.unescape(requested_post.body),
                           comment=comments_form, current_year=YEAR, comments=blog_comments)


@app.route('/new-post', methods=["GET", "POST"])
@admin_only
def new_post():
    """Route for adding new blogs"""
    new_post_form = NewPost(author=current_user.name)
    if new_post_form.validate_on_submit():
        date_today = datetime.today().date()
        month = date_today.strftime("%B")
        day = date_today.strftime("%d")
        blog_year = date_today.strftime("%Y")
        new_post = PostTable(title=new_post_form.title.data, body=new_post_form.body.data,
                             author_id=current_user.id, img_url=new_post_form.img_url.data,
                             subtitle=new_post_form.subtitle.data, date=f'{month} {day}, {blog_year}')

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('make-post.html', form=new_post_form, current_year=YEAR, is_edit=False)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    """Route for editing existing blogs"""
    post_to_update = PostTable.query.get(post_id)
    edit_form = NewPost(
        title=post_to_update.title,
        subtitle=post_to_update.subtitle,
        author=current_user.name,
        img_url=post_to_update.img_url,
        body=post_to_update.body
    )
    if edit_form.validate_on_submit():
        post_to_update.title = edit_form.title.data
        post_to_update.subtitle = edit_form.subtitle.data
        post_to_update.img_url = edit_form.img_url.data
        post_to_update.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_post', post_id=post_to_update.id))

    return render_template("make-post.html", form=edit_form, is_edit=True, post_id=post_id, current_year=YEAR)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    """Deletes existing blogs"""
    post_to_delete = PostTable.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
