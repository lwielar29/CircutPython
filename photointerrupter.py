# Photointerrpter
# Lily Wielar
# Every 4 seconds the serial monitor prints how many times an object passed through the photointerrupter

from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7) #photointerrupter on pin D7
interrupter.direction = Direction.INPUT # setting up photointerrupter - input
interrupter.pull = Pull.UP #setting up photointerrupter 

counter = 0 #counter variable equals 0

photo = False #photo is false/off
state = False #state is false/off

max = 4 #variable max equals 4

start = time.time() #start variable equals time since program started running

while True:
    photo = interrupter.value #"photo" equals the state on interrupter, true or false
    if photo and not state: # if interrupter has been interrupted...
            counter += 1 #add one to counter
    state = photo #ullifies the if so counter only goes up once

    remaining = max - time.time() #variable "remaining" equals 4 minus how long it has been running 

    if remaining <= 0: # if the remaining variable is less than or equal to 0...
        print("Interrupts:", str(counter)) #serial monitor prints the word "interrupts" and counter integer
        max = time.time() + 4 #max equals the running time plus 4
        counter = 0 #resets counter variable to 0
