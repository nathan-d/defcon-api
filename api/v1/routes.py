
from api import common
from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def index():
  return "You've hit the index!"

@api.route('/status', methods=['GET'])
def get_status():
  return common.get_status()
  
@api.route('/status/<int:status>')
def set_status(status):
    return common.set_status(status)
    
@api.route('party', methods=['GET'])
def set_party_mode():
    return common.party_mode()
    