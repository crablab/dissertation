from flask import render_template, url_for, redirect, abort
from flask_login import login_required, current_user


from . import administrator 

@administrator.route("/administrator", methods=["GET", "POST"])
@login_required
def index():
    if current_user.get_permissions != "administrator":
        abort(403) 

    return render_template("administrator.html")