from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapp123'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    add_book = SubmitField('Add Book')


class EditForm(FlaskForm):
    new_rating = FloatField('New Rating', render_kw={"placeholder": "New Rating"}, validators=[DataRequired()])
    change_rating = SubmitField('Change Rating')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        new_book = Book(title=book_form.book_name.data, author=book_form.book_author.data, rating=book_form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=book_form)


@app.route('/edit', methods=["GET", "POST"])
def edit_rating():
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        book_to_update = Book.query.get(request.form['id'])
        book_to_update.rating = edit_form.new_rating.data
        db.session.commit()

        return redirect(url_for('home'))

    book_data = Book.query.filter_by(id=request.args.get('id')).first()
    return render_template('edit_rating.html', form=edit_form, book=book_data)


@app.route('/delete')
def delete_book():
    book_to_delete = Book.query.get(request.args.get('id'))
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
