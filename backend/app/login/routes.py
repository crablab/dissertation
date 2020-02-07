from flask import render_template, url_for, redirect
from ..forms import LoginForm

from . import login

@login.route('/', methods=['GET', 'POST'])
def index():

    form = LoginForm()

    if form.validate_on_submit():
        pass

    return render_template('login.html', form = form)