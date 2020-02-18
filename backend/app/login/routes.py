from flask import render_template, url_for, redirect, abort, flash, request
from flask_login import login_user
from ..forms import LoginForm, SignupForm
from ..libraries import user

from . import login

@login.route('/', methods=['GET', 'POST'])
def index():

    form = LoginForm()

    if form.validate_on_submit():
        usr = user.user()
        if usr.load_user(email=form.email.data) == False:
            failed_login()
        elif usr.check_login(form.password.data):
            # Login with flask_login
            login_user(usr)

            flash('Logged in successfully.')

            return redirect("/student")

        else:
            failed_login()

    return render_template('login.html', form = form)

@login.route('/signup', methods=['GET', 'POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():
        usr = user.user()
        id = usr.create_user(form.name.data, form.email.data, form.password.data, form.type.data)
        print(id)
        if id != False:
            flash('Account created for ' + id)
            return redirect('/')
        else: 
            flash('Error occurred: you\'re probably reusing an email')
            return redirect('/signup')

    return render_template('signup.html', form = form)

def failed_login():
    flash('Epic fail.')
    return redirect('/')