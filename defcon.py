"""DefCon API for the DefCon status system."""
from flask import Flask
from api.v1 import routes as api_v1

APP = Flask(__name__)
APP.register_blueprint(api_v1.api, url_prefix='/v1')

if __name__ == '__main__':
    APP.run(debug=True)
