import time
import config
import random
import gpio_interface as gpio


class Defcon(object):

    def __init__(self):
        self.config = config.Config()
        self.gpio = gpio.Pins(self.config.get_pin_map())
        self.party_mode = False

    def get_status(self):
        return self.config.get_config()['defcon_state']

    def strobe(self, action):
        strobe = self.config.get_config()['strobe_pin']
        if action == 'start':
            pass
            print 'Starting strobe..'
            self.gpio.blind_set(strobe)
            print 'Started.'
        else:
            print 'Ending strobe...'
            self.gpio.unset_pin(strobe)
            print 'Ended.'

    def set_status(self, new_status):
        # self.strobe('start')
        # Play sound - For 1 second
        current_status = self.get_status()
        resp = self.gpio.set_pin(current_status, new_status)
        # self.strobe('stop')
        return resp

    def save_status(self, status):
        self.set_status(status)
        current_conf = self.config.get_config()
        current_conf['defcon_state'] = status
        response = self.config.save_config(current_conf)
        if not response:
            response = 'Error!'
        return response

    def party(self):
        print 'Started'
        light_map = self.config.get_pin_map()
        print 'maps in place'
        while True:
            num_on = random.randint(1, 3)
            activate = random.sample(light_map, num_on)
            self.gpio.unset_all_pins()
            for e in activate:
                print 'Activating light %s' % e
                self.gpio.blind_set(e)
            time.sleep(1)
