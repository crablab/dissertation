from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email


class LoginForm(FlaskForm):
    email = StringField(
        'Email address:', validators=[Required(), Email()])
    password = PasswordField(
        'Password:', validators=[Required()])

    submit = SubmitField('Submit')