from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditor, CKEditorField


# New post form
class NewPost(FlaskForm):
    """Form for adding new blogs"""
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


# Register User form
class RegisterForm(FlaskForm):
    """Form for getting details of new user during registrations"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Sign Me Up!')


# Login existing users
class LoginForm(FlaskForm):
    """Form for getting login details"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Let Me In!')


# New comments form
class CommentsForm(FlaskForm):
    """Form for getting comments from users"""
    comment = CKEditorField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit Comment')
