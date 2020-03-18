from flask import render_template, url_for, redirect, abort
from flask_login import login_required, current_user
from ..libraries import lectures
from ..libraries import upcoming_lectures

from . import student 

@student.route('/student', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.get_permissions != "student":
        abort(403) 

    ucl = upcoming_lectures.upcoming_lectures()
    ucl.load_upcoming(current_user.id)

    lectures = []

    # Turn into JSON and format the time
    for key, course in enumerate(ucl.get_upcoming):
        lectures.append({"id": course.id, "time": course.time.strftime("%c"), "course": course.course})

    return render_template('student.html', data = lectures)