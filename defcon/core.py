"""This module acts as the central file for all DefCon functions."""
import time
import random
import defcon.config as config
import defcon.gpio_interface as gpio


class Defcon(object):
    """Defcon class is the parent class for all Defcon functions.
    Including the GPIO interface bridge. """

    def __init__(self):
        self.config = config.Config()
        self.gpio = gpio.Pins(self.config.get_gpio_conf())
        self.party_mode = False

    def get_status(self):
        """Returns the current status of the Defcon unit."""
        return self.config.get_config()['defcon_state']

    def strobe(self, action):
        """Strobe functionality for event change."""
        strobe = self.config.get_config()['strobe_pin']
        if action == 'start':
            print 'Starting strobe..'
            self.gpio.blind_set(strobe)
            print 'Started.'
        else:
            print 'Ending strobe...'
            self.gpio.unset_pin(strobe)
            print 'Ended.'

    def set_status(self, new_status):
        """Function to set the Defcon status."""
        # self.strobe('start') #TODO: Uncoment when strobe connected to unit
        # Play sound - For 1 second #TODO: Tracked in issue #2
        current_status = self.get_status()
        resp = self.gpio.set_pin(current_status, new_status)
        # self.strobe('stop')
        return resp

    def save_status(self, status):
        """Function to save the Defcon status to Config."""
        self.set_status(status)
        current_conf = self.config.get_config()
        current_conf['defcon_state'] = status
        response = self.config.save_config(current_conf)
        if not response:
            return 'Error!'
        return response

    def party(self):
        """Temporary function for the Party mode functionality."""
        print 'Started'
        party_conf = self.config.get_config()
        random_min = party_conf['party_mode']['min_lights']
        random_max = party_conf['party_mode']['max_lights']
        light_map = self.config.get_gpio_conf()['pin_map']
        while True:
            num_on = random.randint(random_min, random_max)
            activate = random.sample(light_map, num_on)
            self.gpio.unset_all_pins()
            for element in activate:
                print 'Activating light %s' % element
                self.gpio.blind_set(element)
            time.sleep(1)
