from flask import Flask
from .config import config, Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_object(config['development'])

    return app