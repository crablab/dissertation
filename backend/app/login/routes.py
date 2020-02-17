from flask import render_template, url_for, redirect
from ..forms import LoginForm, SignupForm

from . import login

@login.route('/', methods=['GET', 'POST'])
def index():

    form = LoginForm()

    if form.validate_on_submit():
        pass

    return render_template('login.html', form = form)

@login.route('/signup', methods=['GET', 'POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():
        pass

    return render_template('signup.html', form = form)