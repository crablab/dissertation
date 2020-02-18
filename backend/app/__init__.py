from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from app.login.routes import login
from app.student.routes import student

from app.libraries import user

bootstrap = Bootstrap()
login_manager = LoginManager()
# For login manager handler 
usr = user.user()

def create_app():

    app = Flask(__name__)

    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login.index"

    # Blueprints
    app.register_blueprint(login)
    app.register_blueprint(student)
    #app.register_blueprint(api, url_prefix='/api')

    return app

@login_manager.user_loader
def load_user(user_id):
    usr.load_user(user_id)
    return usr