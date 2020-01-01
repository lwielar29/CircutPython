# Servo
# Lily Wielar
# a 180° micro servo slowly sweeps back and forth between 0 and 180°, 
# when you touch one wire and the servo goes one way and when you touch the other wire and it goes the other way

import time   #importing neessary libraries....
import board
import pulseio
import touchio
from adafruit_motor import servo

pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50) # pwm variable equals pulseio pwm ith pin D9 
angle = 5 # variable angle equals 5 

touch_pad = board.A3 # touch_pad equals wire1 on analog pin A3
touch_pad2 = board.A4 # touch_pad2 equals wire2 on analog pin A4

touch = touchio.TouchIn(touch_pad) #touch equals state of touch_pad
touch2 = touchio.TouchIn(touch_pad2) #touch2 equals state of touch_pad2

my_servo = servo.Servo(pwm) #servo equals stipulations of previously defined "pwm"

while True:
    if touch.value: # if touch.value (if wire 1 is touched...)
        print("touched blue!") # serial monitor print "touched blue!"
        if angle < 180: # if wire1 is being touched and is servo angle is less than 180...
            angle += 5 #add 5 to "angle"
        my_servo.angle = angle # move servo to specified "angle"
        time.sleep(0.05) #pause

    if touch2.value: # if touch.value (if wire2 is touched...)
        print("touched green!") # serial monitor print "touched green!"
        if angle > 0: # if wire2 is being touched and is servo angle is greater than 0...
            angle -= 5 # minus 5 to angle
        my_servo.angle = angle # move servo to specified "angle"
        time.sleep(0.05) #pause
