from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired , Email , Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4 , max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4 , max=80)])
    email = StringField('Email', validators=[DataRequired(), Email() , Length(min=4 , max=80)])
    remember_me = BooleanField('remember_me', default=False)

