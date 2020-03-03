from flask import render_template, url_for, redirect, abort
from flask_login import login_required, current_user
from ..forms import AssignmentForm
from ..libraries import users
from ..libraries import lectures

from . import administrator 

@administrator.route("/administrator", methods=["GET", "POST"])
@login_required
def index():
    if current_user.get_permissions != "administrator":
        abort(403) 

    ass_form = AssignmentForm()
    configure_assignment_form(ass_form)

    return render_template("administrator.html", form = ass_form)

def configure_assignment_form(form):
    """
    Takes a flask_wtf object for the assignment form.
    Loads it with the relevant data. 

    :param form: the object for the assignment form
    """
    # Users
    users_class = users.users()
    users_class.load_users()
    usr_choices = []

    for key, value in users_class.users.items():
        user = value.get_user()
        usr_choices.append((key, user['name'] + " (" + user['email'] + ") - " + value.get_permissions))
        # usr_choices.append((user.get_id, user.name + " (" + user.email + ") - " + user.get_permissions))

    form.user.choices = usr_choices

    # Courses 
    lectures_class = lectures.lectures()
    lectures_class.load_distinct_courses()
    course_choices = []

    for key, value in lectures_class.lectures.items():
        course_choices.append((value.id, value.course))
    
    form.course.choices = course_choices

    return