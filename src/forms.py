from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from src.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Inloggen')

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords don\'t match!')])
    pass_confirm = PasswordField('Wachtwoord verifiëren', validators=[DataRequired()])
    submit = SubmitField('Registreren')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            return False
        return True

class EditForm(FlaskForm):
    description = TextAreaField('Beschrijving', validators=[DataRequired()])
    submit = SubmitField('Aanpassen')