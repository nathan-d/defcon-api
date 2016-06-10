import time
import RPi.GPIO as GPIO


class Pins(object):

    def __init__(self, pin_map):
        print pin_map
        self.map = pin_map
        GPIO.setmode(GPIO.BCM)
        self._config_gpio(self.map)

    def set_pin(self, current_state, new_state):
        if self.map[new_state]:
            self.unset_pin(current_state)
            return GPIO.output(self.map[new_state], False)

    def unset_pin(self, id):
        if self.map[id]:
            GPIO.output(self.map[id], True)

    def unset_all_pins(self):
        for id in self.map:
            print 'Unsetting pin %s' % id
            self.unset_pin(id)

    def blind_set(self, pin):
        GPIO.output(self.map[pin], False)

    def pin_test(self):
        for pin in self.map:
            print 'Setting light pin %s' % (pin)
            self.blind_set(self.map[pin])
            time.sleep(0.5)
            self.unset_pin(self.map[pin])

    def _config_gpio(self, pins):
        for id in pins:
            GPIO.setup(pins[id], GPIO.OUT)
            print "Pin %s configured." % id
