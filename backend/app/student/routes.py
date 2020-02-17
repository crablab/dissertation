from flask import render_template, url_for, redirect

from . import student

@student.route('/student', methods=['GET', 'POST'])
def index():

    return render_template('student.html')
