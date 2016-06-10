import yaml
import time


class Config(object):

    def __init__(self):
        self.config = self.load_config()
        self.config_timestamp = time.time()

    def get_config(self):
        return self.config

    def get_pin_map(self):
        return self.config['pin_map']

    def load_config(self):
        conf = dict()
        try:
            with open('config.yml', 'r+') as stream:
                conf = yaml.load(stream)
                print 'Config loaded.'
        except Exception:
            print 'Unable to open config file.'
        return conf

    def save_config(self, data):
        try:
            with open('config.yml', 'w') as outfile:
                outfile.write(yaml.dump(data, default_flow_style=False))
                print 'Config saved.'
            self.config = data
            return True
        except:
            print 'Unable to save config file.'
