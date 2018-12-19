from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
<<<<<<< HEAD
from wtforms.validators import DataRequired
=======
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

>>>>>>> 6d89c72c3471fde89a361ec9709c478bc9e19a08

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
<<<<<<< HEAD
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
=======
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
>>>>>>> 6d89c72c3471fde89a361ec9709c478bc9e19a08
