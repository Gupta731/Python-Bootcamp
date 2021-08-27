from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

MOVIE_DB_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = os.environ.get('MOVIE_DB_API_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapp123'
Bootstrap(app)

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top10.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Edit Rating and Review form
class EditForm(FlaskForm):
    rating = FloatField("Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    update_button = SubmitField("Done")


# Add movie form
class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    add_button = SubmitField("Add Movie")


# Movies table in top10 database
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(5), nullable=False)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(300), nullable=False)


# db.create_all()

def add_movies_to_db(movie_details):
    """Add a record to Movies table"""
    new_movie = Movies(title=movie_details['title'],
                       year=movie_details['release_date'].split('-')[0],
                       description=movie_details['overview'],
                       rating=movie_details['vote_average'],
                       ranking=0,
                       review="",
                       img_url=f"{MOVIE_DB_IMAGE_URL}/{movie_details['poster_path']}")
    db.session.add(new_movie)
    db.session.commit()
    return new_movie.id


def get_movie_details(title):
    """Gets details of the all movies with the name provided by user"""
    movie_db_parameters = {
        'api_key': MOVIE_DB_API_KEY,
        'query': title,
        'language': 'en-US',
        'include_adult': 'false'
    }
    response = requests.get(url=MOVIE_DB_URL, params=movie_db_parameters)
    response.raise_for_status()
    movie_data = response.json()['results']
    return movie_data


@app.route("/")
def home():
    all_movies = Movies.query.order_by(Movies.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_rating_review():
    """Updates the rating and review for the movies as provided by user"""
    edit_form = EditForm()
    movie_id = request.args.get('id')
    movie_to_update = Movies.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=edit_form, movie=movie_to_update)


@app.route('/add', methods=["POST", "GET"])
def add_movie():
    """Adds a movie to database which shows up in website home page"""
    add_form = AddForm()
    if add_form.validate_on_submit():
        all_movies_data = get_movie_details(add_form.movie_title.data)
        return render_template('select.html', data=all_movies_data)

    return render_template('add.html', form=add_form)


@app.route('/delete')
def delete_movie():
    """Deletes a movie from the database on request from the user"""
    movie_to_delete = Movies.query.get(request.args.get('id'))
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/find")
def get_movie_details_by_id():
    """Gets details of the movies based on movie id of the selected movie"""
    movie_id = request.args.get('id')
    movie_db_parameters = {
        'api_key': MOVIE_DB_API_KEY,
        'language': 'en-US',
    }
    response = requests.get(url=f"{MOVIE_DB_INFO_URL}/{movie_id}", params=movie_db_parameters)
    response.raise_for_status()
    movie_details = response.json()
    get_id = add_movies_to_db(movie_details)
    return redirect(url_for('edit_rating_review', id=get_id))


if __name__ == '__main__':
    app.run(debug=True)
