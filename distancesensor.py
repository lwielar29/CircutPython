# Distance Censor
# Lily Wielar
# sensing distance from object to monitor and correlate light color on metroexpress to distance - https://www.rapidtables.com/web/color/RGB_Color.html

import time # adding time libraries 
import board # adding board libraries 
import neopixel # adding neopixel libraries
import simpleio # adding simpleio libraries
import adafruit_hcsr04 # add adafruit distance censor library 
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D7) # sonar equals distance sensor with pins D6 and D7
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1) #dot equals metroexpress board led

red = 0 # variable red 
green = 0 # variable green 
blue = 0 # variable blue 

while True:

    try: #attempt....
        sonarValue = sonar.distance # sonarvalue equals the distance object is from censor
        print(sonarValue) # serial monitor prints value/distance
        if sonarValue < 5: #if the distance is less than 5...
            dot.fill((255, 0, 0)) # led is red
        if sonarValue > 35: #if the distance is greater than 35...
            dot.fill((0, 255, 0)) # led is green
        if sonarValue <= 20 and sonarValue > 5: #if distance is between 5 and 20...
            red = simpleio.map_range(sonarValue, 6, 20, 255, 0) # red pixel correlates to distance where 6 equals full red and 20 equals no red
            blue = simpleio.map_range(sonarValue, 6, 20, 0, 255) # blue pixel correlates to distance where 6 equals no blue and 20 equals full blue
            green = 0 # no green
        if sonarValue <= 35 and sonarValue > 20: #if the distance is between 20 and 35...
            red = 0 # no red
            blue = simpleio.map_range(sonarValue, 21, 35, 255, 0)# blue pixel correlates to distance where 21 equals full blue and 35 equals no blue
            green = simpleio.map_range(sonarValue, 21, 35, 0, 255)# green pixel correlates to distance where 21commenti equals no green and 35 equals full green
        dot.fill((int(red), int(green), int(blue))) #led is composed of RGB pixels...fill with corresponding values

    except RuntimeError: # when theres a runtime error...
        print("retrying") #print on serial monitor "retrying"
        pass 

    time.sleep(0.1) #wait 1 second
