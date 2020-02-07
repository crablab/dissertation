from flask import render_template, url_for, redirect

from . import login

@login.route('/', methods=['GET', 'POST'])
def index():

    return render_template('login.html')