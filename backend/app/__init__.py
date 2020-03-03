from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user
from flask_allows import Allows, Requirement

from app.login.routes import login
from app.student.routes import student
from app.administrator.routes import administrator

from app.libraries import user

bootstrap = Bootstrap()
login_manager = LoginManager()

def create_app():

    app = Flask(__name__)

    bootstrap.init_app(app)
    login_manager.init_app(app)
    allows = Allows(app=app, identity_loader=lambda: current_user)
    login_manager.login_view = "login.index"

    # Blueprints
    app.register_blueprint(login)
    app.register_blueprint(student)
    app.register_blueprint(administrator)
    #app.register_blueprint(api, url_prefix='/api')

    return app

# Application wide code to handle login and RBAC

# Login manager user hook
@login_manager.user_loader
def load_user(user_id):
    usr = user.user()
    usr.load_user(user_id)
    return usr