from flask import render_template, url_for, redirect, abort, flash
from flask_login import login_required, current_user
from ..forms import AssignmentForm
from ..libraries import users
from ..libraries import lectures
from ..libraries import allocation

from . import administrator 

@administrator.route("/administrator", methods=["GET", "POST"])
@login_required
def index():
    if current_user.get_permissions != "administrator":
        abort(403) 

    ass_form = AssignmentForm()
    configure_assignment_form(ass_form)

    if ass_form.validate_on_submit():
        # Create the allocation 
        allocation_class = allocation.allocation()

        if allocation_class.allocate(ass_form.user.data, ass_form.course.data) != False:
            flash("Allocated successfully")
        else:
            flash("Allocation failed")
        

    return render_template("administrator.html", form = ass_form, data = get_courses())

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

        usr_choices.append((key, value.name + " (" + value.email + ") - " + value.get_permissions))

    form.user.choices = usr_choices

    # Courses 
    course_choices = []

    # Tuplify for select HTML item
    for course in get_courses():
        course_choices.append((course, course))

    form.course.choices = course_choices

    return

def get_courses():
    lectures_class = lectures.lectures()
    lectures_class.load_distinct_courses()
    courses = []

    for key, value in lectures_class.lectures.items():
        courses.append(value.course)

    return courses