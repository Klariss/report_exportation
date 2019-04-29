from flask import Flask

from settings import DevConfig
from rest import report_pdf


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(report_pdf.blueprint)
    return app
