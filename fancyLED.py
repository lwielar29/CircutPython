import time
from digitalio import DigitalInOut, Direction, Pull  #pylint: disable-msg=import-error
import random
import board   #pylint: disable-msg=import-error

class FancyLED:
    def __init__ (self, pin1, pin2, pin3):
        self.pin1 = DigitalInOut(pin1)
        self.pin1.direction = Direction.OUTPUT

        self.pin2 = DigitalInOut(pin2)
        self.pin2.direction = Direction.OUTPUT

        self.pin3 = DigitalInOut(pin3)
        self.pin3.direction = Direction.OUTPUT

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