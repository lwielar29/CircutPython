import time
import board
import neopixel
import simpleio
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D7)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)

red = 0
green = 0
blue = 0

while True:

    try:
        sonarValue = sonar.distance
        print(sonarValue)
        if sonarValue < 5:
            dot.fill((255, 0, 0))
        if sonarValue > 35:
            dot.fill((0, 255, 0))
        if sonarValue <= 20 and sonarValue > 5:
            red = simpleio.map_range(sonarValue, 6, 20, 255, 0)
            blue = simpleio.map_range(sonarValue, 6, 20, 0, 255)
            green = 0
        if sonarValue <= 35 and sonarValue > 20:
            red = 0
            blue = simpleio.map_range(sonarValue, 21, 35, 255, 0)
            green = simpleio.map_range(sonarValue, 21, 35, 0, 255)
        dot.fill((int(red), int(green), int(blue)))

    except RuntimeError:
        print("retrying")
        pass

    time.sleep(0.1)