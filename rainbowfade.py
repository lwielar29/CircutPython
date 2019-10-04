import pulseio
import time

class RGB:

    full = 65535

    def __init__(self, red, green, blue):
        self.r = pulseio.PWMOut(red, frequency=5000, duty_cycle=0)
        self.g = pulseio.PWMOut(green, frequency=5000, duty_cycle=0)
        self.b = pulseio.PWMOut(blue, frequency=5000, duty_cycle=0)


    def red(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 65535
        self.b.duty_cycle = 65535

    def blue(self):
        self.r.duty_cycle = 65535
        self.g.duty_cycle = 65535
        self.b.duty_cycle = 0

    def green(self):
        self.r.duty_cycle = 65535
        self.g.duty_cycle = 0
        self.b.duty_cycle = 65535

    def cyan(self):
        self.r.duty_cycle = 65535   # 0% red
        self.g.duty_cycle = 0    # 100% green
        self.b.duty_cycle = 0

    def yellow(self):
        self.r.duty_cycle = 0   # 100% red
        self.g.duty_cycle = 0     # 100% green
        self.b.duty_cycle = 65535

    def magenta(self):
        self.r.duty_cycle = 0   # 100% red
        self.g.duty_cycle = 65535     # 0% green
        self.b.duty_cycle = 0  # 100% blue

    def rainbow(self, x):
        print("rainbow")
        if x == "rate1":
            self.r.duty_cycle = 0
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = (self.full)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = i
                self.b.duty_cycle = (self.full)
                self.g.duty_cycle = (self.full)-i
                time.sleep(.000001)
            for i in range (5, 65535, 5):
                self.r.duty_cycle = (self.full)
                self.b.duty_cycle = (self.full)-i
                self.g.duty_cycle = i
                time.sleep(.000001)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = (self.full)-i
                self.b.duty_cycle = i
                self.g.duty_cycle = (self.full)
                time.sleep(.000001)

        elif x == "rate2":
            self.r.duty_cycle = 0
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = (self.full)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = i
                self.b.duty_cycle = (self.full)
                self.g.duty_cycle = (self.full)-i
                time.sleep(.000001)
            for i in range (5, 65535, 5):
                self.r.duty_cycle = (self.full)
                self.b.duty_cycle = (self.full)-i
                self.g.duty_cycle = i
                time.sleep(.000001)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = (self.full)-i
                self.b.duty_cycle = i
                self.g.duty_cycle = (self.full)
                time.sleep(.000001)