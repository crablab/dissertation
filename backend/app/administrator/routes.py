from flask import render_template, url_for, redirect, abort
from flask_login import login_required, current_user
from ..forms import AssignmentForm

from . import administrator 

@administrator.route("/administrator", methods=["GET", "POST"])
@login_required
def index():
    if current_user.get_permissions != "administrator":
        abort(403) 

    ass_form = AssignmentForm()
    configure_form(ass_form)

    return render_template("administrator.html", form = ass_form)

def configure_form(form):
    form.user.choices = [("user1", "user1")]
    form.course.choices = [("course2", "course2")]

    return