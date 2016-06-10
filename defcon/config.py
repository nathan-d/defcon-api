"""Config module for the DefCon application."""
import time
import yaml


class Config(object):
    """Handles the config file loading and exposes some sub-elements through functions."""

    def __init__(self):
        self.config = self._load_config()
        self.config_timestamp = time.time()

    def get_config(self):
        """Returns config object to external classes."""
        return self.config

    def get_gpio_conf(self):
        """Returns the GPIO configuration struct."""
        return self.config['gpio_interface']

    def save_config(self, data):
        """Saves the config file."""
        try:
            with open('config.yml', 'w') as outfile:
                outfile.write(yaml.dump(data, default_flow_style=False))
                print 'Config saved.'
            self.config = data
            return True
        except IOError:
            print 'Unable to save config file.'

    @staticmethod
    def _load_config():
        """Loads the config file."""
        conf = dict()
        try:
            with open('config.yml', 'r+') as stream:
                conf = yaml.load(stream)
                print 'Config loaded.'
        except IOError:
            print 'Unable to open config file.'
        return conf
