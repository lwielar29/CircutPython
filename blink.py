import board
import digitalio
import time

led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT
led.value = True
led.value = False