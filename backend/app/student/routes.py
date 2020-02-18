from flask import render_template, url_for, redirect
from flask_login import login_required
from . import student

@student.route('/student', methods=['GET', 'POST'])
@login_required
def index():

    return render_template('student.html')
