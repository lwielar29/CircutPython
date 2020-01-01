#Rainbow
# Lily Wielar
# creating class RGB to run with assigned code that makes three RGB leds flash different colors

class RGB: #class name RGB
    def__init__(self, red, green, blue): #automatically creates functions red, green, blue
       self.red = pulseio.PWMOut(red)  # red will pulseio PWM with pin "red"
       self.green = pulseio.PWMOut(green) # green will pulseio PWM with pin "green"
       self.blue = pulseio.PWMOut(blue) # blue will pulseio PWM with pin "blue"


def red (self): # function red...
red.duty_cycle = 65535 # 100% red
green.duty_cycle = 0   # 0% green
blue.duty_cycle = 0  # 0% blue

def blue (self): # function blue...
red.duty_cycle = 0 # 0% red
green.duty_cycle = 0   # 0% green
blue.duty_cycle = 65535   # 100% blue

def green (self): # function green...
red.duty_cycle = 0 # 0% red
green.duty_cycle = 65535 # 100% green
blue.duty_cycle = 0  # 100% blue

def cyan(self): # function cyan...
red.duty_cycle = 0   # 0% red
green.duty_cycle = 65535    # 100% green
blue.duty_cycle = 65535  # 100% blue

def yellow(self): # function yellow...
red.duty_cycle = 65535   # 100% red
green.duty_cycle = 65535     # 100% green
blue.duty_cycle = 0    #0% blue

def magenta(self): # function magenta...
red.duty_cycle = 65535   # 100% red
green.duty_cycle = 0     # 0% green
blue.duty_cycle = 65535  # 100% blue
