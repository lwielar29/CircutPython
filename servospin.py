import time
import board
import pulseio
import touchio
from adafruit_motor import servo

pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
angle = 5

touch_pad = board.A3
touch_pad2 = board.A4

touch = touchio.TouchIn(touch_pad)
touch2 = touchio.TouchIn(touch_pad2)

my_servo = servo.Servo(pwm)

while True:
    if touch.value:
        print("touched blue!")
        if angle < 180:
            angle += 5
        my_servo.angle = angle
        time.sleep(0.05)

    if touch2.value:
        print("touched green!")
        if angle > 0:
            angle -= 5
        my_servo.angle = angle
        time.sleep(0.05)