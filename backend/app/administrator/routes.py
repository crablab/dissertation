from flask import render_template, url_for, redirect, abort, flash
from flask_login import login_required, current_user
from ..forms import AssignmentForm, AddLecture
from ..libraries import users, lectures, lecture, allocation

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


@administrator.route("/administrator/course/<path:text>", methods=["GET", "POST"])
# @login_required
def courses(text):
    # if current_user.get_permissions != "administrator":
    #     abort(403) 

    # Initiate the form 
    adl_form = AddLecture()

    # If the form was submitted...
    if adl_form.validate_on_submit():
        lecture_class = lecture.lecture()
        if lecture_class.create_lecture(adl_form.course.data, adl_form.datetime.data):
            flash("Lecture created successfully")
        else:
            flash("Lecture creation failed")

    # Generate the table data
    lectures_class = lectures.lectures()
    courses = lectures_class.load_lectures(course = text)

    if courses == False:
        abort(500)
    
    courses_dict = []

    for key, course in lectures_class.lectures.items():
        courses_dict.append({"id": course.id, "time": course.time.strftime("%c")})
    
    return render_template("course.html", form = adl_form, data = {"code": text, "lectures": courses_dict})


# Helper methods

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
    """
    Gets the distinct list of course objects.

    :returns: List of distinct course objects.
    """
    lectures_class = lectures.lectures()
    lectures_class.load_distinct_courses()
    courses = []

    for key, value in lectures_class.lectures.items():
        courses.append(value.course)

    return courses