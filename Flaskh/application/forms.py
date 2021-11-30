from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User, Savedcode
from flask import request


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=150)])
    password_confirm = PasswordField("Confirm Password",
                                     validators=[DataRequired(), Length(min=6, max=150), EqualTo('password')])

    submit = SubmitField("Register now")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use!, please use other email")


class Compiler(FlaskForm):
    title = TextAreaField("title")
    description = TextAreaField("description")
    code = TextAreaField("code")
    input = TextAreaField("input")
    output = TextAreaField("output")
    language = SelectField("language", choices=['C', 'C++', 'Java', 'Python', 'C#'])
    Run = SubmitField("Run")
    Save = SubmitField("Save")
    Download = SubmitField("Download")
    Stop = SubmitField("Stop")
    Share = SubmitField("Share")


class Saved_code(FlaskForm):
    Edit = SubmitField("Edit")
    Delete = SubmitField("Delete")
    Download = SubmitField("Download")

    def validate_title(self, title):
        user = Savedcode.objects(email=title.data).first()
        if user:
            raise ValidationError("Email is already in use!, please use other email")
