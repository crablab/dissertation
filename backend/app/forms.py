from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField(
        'Email address:', validators=[Required(), Email()])
    password = PasswordField(
        'Password:', validators=[Required()])

    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    name = StringField('Name:', validators=[Required()])
    email = StringField('Email address:', validators=[Required(), Email()])
    password = PasswordField('New Password', [Required(), EqualTo('passwordconfirm', message='Passwords must match')])
    passwordconfirm  = PasswordField('Repeat Password')
    type = SelectField('User Type', choices = [('student','Student'), ('lecturer','Lecturer'), ('administrator','Administrator')], validators = [Required()])

    submit = SubmitField('Submit')