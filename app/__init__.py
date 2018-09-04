from flask import Flask
from config import config_options


def create_app(config_name):
    #  app will be initailized when this function is called from the manage file.
    app = Flask(__name__)

    # setting up configurations
    app.config.from_object(config_options[config_name])

    # regestering blueprints at this point so that they can be instantiated when the app is run
    #  start by importing the blueprint to be registered
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # since the api keys are outside the blueprint I must call the configure requests function from the blueprint and pass in the main app as argument so that it can get the apis from the main app
    from .requests import configure_requests
    configure_requests(app)

    return app
