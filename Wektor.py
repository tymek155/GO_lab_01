import Punkt

class Wektor:
    def __init__(self, a: type[Punkt], b: type[Punkt]):
        if a.x < b.x:
            self.pkt_1 = a
            self.pkt_2 = b
        else:
            self.pkt_1 = b
            self.pkt_2 = a