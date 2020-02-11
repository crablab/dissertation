from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app.login.routes import login
from app.student.routes import student

bootstrap = Bootstrap()
db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app():

    app = Flask(__name__)

    # Should be in config/ENV
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://registration:4tpbeW7Ak2K9pete#@localhost/registration'

    bootstrap.init_app(app)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    # Blueprints
    app.register_blueprint(login)
    app.register_blueprint(student)
    #app.register_blueprint(api, url_prefix='/api')

    return app
