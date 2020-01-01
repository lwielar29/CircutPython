# Fancy LED Class
# Lily Wielar
# Class for fancy LED assignment that enables given code to alternate, blink, chase, and sparkle 6 leds - for loop
# https://learn.adafruit.com/circuitpython-101-list-and-things-iterators-generators/generators

import time
from digitalio import DigitalInOut, Direction, Pull  #pylint: disable-msg=import-error ## from digitalio library import JUST DigitalInOut, Direction, Pull
import random
import board   #pylint: disable-msg=import-error

class FancyLED: #class name is FancyLED
    def __init__ (self, pin1, pin2, pin3): #automatically creates pin1, pin2, pin3 variables, pins are leds
        self.pin1 = DigitalInOut(pin1) #led1's pin will be "pin1"
        self.pin1.direction = Direction.OUTPUT # pin1 is output

        self.pin2 = DigitalInOut(pin2) #led2's pin will be "pin1"
        self.pin2.direction = Direction.OUTPUT # pin2 is output

        self.pin3 = DigitalInOut(pin3) #led3's pin will be "pin1"
        self.pin3.direction = Direction.OUTPUT # pin3 is output

    def alternate(self): #defining function "alternate"
        for i in range(0,5): # runs 5 times
            self.pin1.value = True #led1 ON
            self.pin2.value = False #led2 off
            self.pin3.value = True #led3 ON
            time.sleep(.5) #pause
            self.pin1.value = False #led1 off
            self.pin2.value = True #led2 ON
            self.pin3.value = False #led3 off
            time.sleep(.5) #pause

        self.pin2.value = False # turns LED2 off
        time.sleep(.5) #pause

    def blink(self): #defining function "blink"
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

    def chase(self): #defining function "chase"
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

    def sparkle(self): #defining function "sparkle"
        for whatever in range(0,5): #runs 5 times
            print (whatever)
            n= random.randint(0,3) #n equals random number 0, 1, 2, or 3
            print("n") #serial print integer 0, 1, 2, 3
            if n==0: #if the random number is 0...
                self.pin1.value = True
                self.pin2.value = True
                self.pin3.value = True
            if n==1: #if the random number is 1...
                self.pin1.value = False
                self.pin2.value = False
                self.pin3.value = True
            if n==2: #if the random number is 2...
                self.pin1.value = True
                self.pin2.value = False
                self.pin3.value = False
            if n==3: #if the random number is 3...
                self.pin1.value = False
                self.pin2.value = True
                self.pin3.value = False
            time.sleep(.5) #pause
            self.pin1.value = False #turn led off
            self.pin2.value = False #turn led off
            self.pin3.value = False #turn led off
