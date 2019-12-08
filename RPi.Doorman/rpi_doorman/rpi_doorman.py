#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
from sensor import Sensor


class Doorman(Sensor):

    NAME = 'Magnetic_Contact'
    PIN = 16

    sensor_state = 0
    door_state = 2  # Set unknown value, due to initial reading
    door_closed = 0
    door_open = 1

    def get_door_state(self):
        if self.door_state == self.door_open:
            return 'Magnetic contact is open'
        else:
            return 'Magnetic contact is closed'

    def sensor_read_callback(self):
        self.sensor_state = 1  # self.GPIO.input(self.PIN)

        if self.sensor_state != self.door_state:
            self.logger.debug('Changing magnetic contact state from %s to %s', self.door_state, self.sensor_state)
            self.door_state = self.sensor_state
            self.logger.info(self.get_door_state())
