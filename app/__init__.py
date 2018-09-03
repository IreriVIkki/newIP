from flask import Flask

def create_app(config_name):
    #  app will be initailized when this function is called from the manage file.
    app = Flask(__name__)

    # regestering blueprints at this point so that they can be instantiated when the app is run
    #  start by importing the blueprint to be registered
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)