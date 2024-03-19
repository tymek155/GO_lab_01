import math

class Punkt:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def oblicz_dlugosc(self, pkt):
        return math.sqrt((pkt.x - self.x)**2 + (pkt.y - self.y)**2)
