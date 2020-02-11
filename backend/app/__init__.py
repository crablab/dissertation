from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app.login.routes import login
from app.student.routes import student

bootstrap = Bootstrap()
db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app(config = None):

    app = Flask(__name__)

    # Load a configuration if provided
    if config is not None:
        app.config.from_object(config)

    bootstrap.init_app(app)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    # Blueprints
    app.register_blueprint(login)
    app.register_blueprint(student)
    #app.register_blueprint(api, url_prefix='/api')

    return app
