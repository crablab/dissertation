from flask import render_template, url_for, redirect

from . import login

@site.route('/', methods=['GET', 'POST'])
def index():

    return render_template('login.html')