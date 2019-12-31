# Fancy LED Class
# Lily Wielar
# Class for fancy LED assignment that enables given code to alternate, blink, chase, and sparkle 6 leds

import time
from digitalio import DigitalInOut, Direction, Pull  #pylint: disable-msg=import-error ## from digitalio library import JUST DigitalInOut, Direction, Pull
import random
import board   #pylint: disable-msg=import-error

class FancyLED: #class name is FancyLED
    def __init__ (self, pin1, pin2, pin3): #automatically creates pin1, pin2, pin3 variables
        self.pin1 = DigitalInOut(pin1) #pin1's pin will be "pin1"
        self.pin1.direction = Direction.OUTPUT # pin1 is output

        self.pin2 = DigitalInOut(pin2) #pin2's pin will be "pin1"
        self.pin2.direction = Direction.OUTPUT # pin2 is output

        self.pin3 = DigitalInOut(pin3) #pin3's pin will be "pin1"
        self.pin3.direction = Direction.OUTPUT # pin3 is output

    def alternate(self):
        for i in range(0,5):
            self.pin1.value = True
            self.pin2.value = False
            self.pin3.value = True
            time.sleep(.5)
            self.pin1.value = False
            self.pin2.value = True
            self.pin3.value = False
            time.sleep(.5)

        self.pin2.value = False
        time.sleep(.5)

    def blink(self):
        self.pin1.value = True
        self.pin2.value = True
        self.pin3.value = True
        time.sleep(1)
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False
        time.sleep(1)
        self.pin1.value = True
        self.pin2.value = True
        self.pin3.value = True
        time.sleep(1)
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False
        time.sleep(1)

    def chase(self):
        self.pin1.value = True
        self.pin2.value = False
        self.pin3.value = False
        time.sleep(.5)
        self.pin1.value = False
        self.pin2.value = True
        self.pin3.value = False
        time.sleep(.5)
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = True
        time.sleep(.5)
        self.pin3.value = False

    def sparkle(self):
        for whatever in range(0,50):
            print (whatever)
            n= random.randint(0,3)
            print("n")
            if n==0:
                self.pin1.value = True
                self.pin2.value = True
                self.pin3.value = True
            if n==1:
                self.pin1.value = False
                self.pin2.value = False
                self.pin3.value = True
            if n==2:
                self.pin1.value = True
                self.pin2.value = False
                self.pin3.value = False
            if n==3:
                self.pin1.value = False
                self.pin2.value = True
                self.pin3.value = False
            time.sleep(.5)
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False
