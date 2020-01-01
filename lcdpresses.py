# LCD button presses
# Lily Wielar
# counts how many times a button was pressed and displays this number on an LCD screen

import time 
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD # import necessary LCD libraries 
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface 
from lcd.lcd import CursorMode
lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16) # sets up LCD screen, 2 x 16

redbutton = digitalio.DigitalInOut(board.D2) #redbutton on pin D2
redbutton.direction = digitalio.Direction.INPUT # button is on output
redbutton.pull = digitalio.Pull.UP #pulling voltage direction

lcd.print("pushes ") #prints the word pushes on LCD screen
presses = 0 #variable "pushes" equals 0

lcd.set_cursor_mode(CursorMode.LINE) #moves the cursor down a line on LCD screen for future prints

while True:
    if redbutton.value: # if the redbutton isn't pressed...
        lcd.set_cursor_pos(1, 4) #setting cursor position
        lcd.print("PRESSES")
    else: # when the button is pressed...
        lcd.set_cursor_pos(1, 4) #setting cursor position
        presses += 1 # add 1 to the presses variable
        lcd.print(presses) # prints number of presses
        time.sleep
