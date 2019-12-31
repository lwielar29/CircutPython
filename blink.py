# LED Blink
# Lily Wielar
# turning LED on and off repeatedly - https://learn.adafruit.com/arduino-to-circuitpython

import board # adding board libraries to reigster metroexpress board
import digitalio # adding digital libraries
import time # adding time libraries

led = digitalio.DigitalInOut(board.A1) # LED pin = A1 on board
led.direction = digitalio.Direction.OUTPUT # LED is output 
led.value = True # LED is on
led.value = False # LED is off
