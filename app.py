from flask import Flask, Blueprint, jsonify
from api.v1 import routes as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1.api, url_prefix='/v1')
    
if __name__ == '__main__':
  app.run(debug=True)
    