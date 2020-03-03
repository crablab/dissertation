from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField(
        'Email address:', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password:', validators=[DataRequired()])

    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email address:', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', [DataRequired(), EqualTo('passwordconfirm', message='Passwords must match')])
    passwordconfirm  = PasswordField('Repeat Password')
    type = SelectField('User Type', choices = [('student','Student'), ('lecturer','Lecturer'), ('administrator','Administrator')], validators = [DataRequired()])

    submit = SubmitField('Submit')

class AssignmentForm(FlaskForm):
    user = SelectField('User', coerce=str, validators=[DataRequired()])
    course = SelectField('Course', coerce=str, validators=[DataRequired()])

    submit = SubmitField('Submit')