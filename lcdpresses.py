import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)

redbutton = digitalio.DigitalInOut(board.D2)
redbutton.direction = digitalio.Direction.INPUT
redbutton.pull = digitalio.Pull.UP

lcd.print("pushes ")
presses = 0

lcd.set_cursor_mode(CursorMode.LINE)

while True:
    if redbutton.value:
        lcd.set_cursor_pos(1, 4)
        lcd.print("PRESSES")
    else:
        lcd.set_cursor_pos(1, 4)
        presses += 1
        lcd.print(presses)
        time.sleep