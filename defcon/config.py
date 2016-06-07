import yaml

class Defcon(object):

  def __init__(self):
    config = _load_config()
    state = config['defcon_state']

  def _load_config():
      conf = dict()
      try: 
          with open('config.yaml', 'r+') as stream:
              conf = yaml.load(stream)
          except:
              print 'Unable to open config file'
      return conf