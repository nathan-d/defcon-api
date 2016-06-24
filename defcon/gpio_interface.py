"""Module to abstract the GPIO calls from the RPi.GPIO lib."""
import time
import RPi.GPIO as GPIO


class Pins(object):
    """Pins class acts as an abstraction layer for GPIO interaction."""

    def __init__(self, conf):
        self.conf = conf
        self.pin_map = self.conf['pin_map']
        GPIO.setmode(GPIO.BCM)
        self._config_gpio(self.pin_map)

    def set_pin(self, current_state, new_state):
        """Unsets the currently active pin before setting a new one."""
        if self.conf.pin_map[new_state]:
            self.unset_pin(current_state)
            return GPIO.output(self.pin_map[new_state], False)

    def unset_pin(self, pin):
        """Unsets the specified pin."""
        if self.pin_map[pin]:
            GPIO.output(self.pin_map[pin], True)

    def unset_all_pins(self):
        """Unsets all pins - Used for party mode."""
        for pin in self.pin_map:
            print 'Unsetting pin %s' % pin
            self.unset_pin(pin)

    def blind_set(self, pin):
        """Sets a pin without unsetting any other pin."""
        GPIO.output(self.pin_map[pin], False)

    def pin_test(self):
        """Test method to check pin map."""
        for pin in self.pin_map:
            print 'Setting light pin %s' % (pin)
            self.blind_set(self.pin_map[pin])
            time.sleep(self.conf['party_mode']['change_delay'])
            self.unset_pin(self.pin_map[pin])

    @staticmethod
    def _config_gpio(pins):
        """Private function to setup the GPIO interface initially."""
        for pin in pins:
            GPIO.setup(pins[pin], GPIO.OUT)
            print "Pin %s configured." % pin
