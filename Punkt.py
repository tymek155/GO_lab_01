import math

class Punkt:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __eq__n__(self, other):
        return self.x == other.x and self.y == other.y

    def oblicz_dlugosc(self, pkt):
        return math.sqrt((pkt.x - self.x)**2 + (pkt.y - self.y)**2)

def k_fun_y(punkt):
    return punkt.y
