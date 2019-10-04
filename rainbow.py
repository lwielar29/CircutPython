class RGB:
    def__init__(self, red, green, blue):
       self.red = pulseio.PWMOut(red,)
       self.green = pulseio.PWMOut(green)
       self.blue = pulseio.PWMOut(blue)


def red (self):
red.duty_cycle = 0
green.duty_cycle = 0
blue.duty_cycle = 65535

def blue (self):
red.duty_cycle = 0
green.duty_cycle = 0
blue.duty_cycle = 65535

def green (self):
red.duty_cycle = 0
green.duty_cycle = 65535
blue.duty_cycle = 0

def cyan(self):
red.duty_cycle = 0   # 0% red
green.duty_cycle = 65535    # 100% green
blue.duty_cycle = 65535

def yellow(self):
red.duty_cycle = 65535   # 100% red
green.duty_cycle = 65535     # 100% green
blue.duty_cycle = 0

def magenta(self):
red.duty_cycle = 65535   # 100% red
green.duty_cycle = 0     # 0% green
blue.duty_cycle = 65535  # 100% blue