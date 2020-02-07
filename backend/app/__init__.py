from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app():

    app = Flask(__name__)

    bootstrap.init_app(app)

    # Blueprints
    app.register_blueprint(login)
    app.register_blueprint(api, url_prefix='/api')
    
    return app
