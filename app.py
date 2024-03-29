import json

from flask import Flask

from flask_cors import CORS
from marshmallow import ValidationError

from ma import ma

from modules.api import api_bp


def create_app():
    """Create an application."""

    app = Flask(__name__)

    CORS(app)
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    ma.init_app(app)

    app.register_blueprint(api_bp, url_prefix='/api')

    @app.errorhandler(ValidationError)
    def register_validation_error(error):
        rv = dict({'message': json.dumps(error.messages)})
        return rv, 422

    print(app.url_map)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
