from api import common
from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def index():
  return "You've hit the index!"

@api.route('/status', methods=['GET'])
def get_status():
  return str(common.get_status())
  
@api.route('/status/up', methods=['GET'])
def status_up():
  return str(common.increment_status())

@api.route('/status/down', methods=['GET'])
def status_down():
  return str(common.decrement_status)

@api.route('/status/<int:status>')
def set_status(status):
    return str(common.set_status(status))
    
@api.route('/party', methods=['GET'])
def set_party_mode():
    return common.party_mode()
    