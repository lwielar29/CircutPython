import time # adding time libraries
import board # adding board libraries
import pulseio # adding pulseio libraries to enable fade similar to analog

led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0) #naming led output, pin, frequency and duty cycle of pulse(PWM)

while True: 
    for i in range(100):  # PWM LED up and down
        if i < 50: #half the time
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else: # the other half
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(0.03) # wait for .3 seconds
