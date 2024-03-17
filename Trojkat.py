import Punkt
from Punkt import Punkt

class Trojkat:
    def __init__(self, p1: type[Punkt], p2: type[Punkt], p3: type[Punkt]):
        if (p1.x == p2.x == p2.x) and (p1.y == p2.y == p3.y) :
            print("Nie mozna utworzyc trojkata!")
        else:
            self.t1 = p1
            self.t2 = p2
            self.t3 = p3

    def trojkat_wspolcznniki_spr(self, wsp1, wsp2):
        if (wsp1[0] * wsp2[1] - wsp2[0] * wsp1[1]) == 0:
            print("Proste rownolegle!")
            return None
        else:
            px = ((wsp2[2] * wsp1[1] - wsp1[2] * wsp2[1]) / (wsp1[0] * wsp2[1] - wsp2[0] * wsp1[1]))
            py = ((wsp2[0] * wsp1[2] - wsp1[0] * wsp2[2]) / (wsp1[0] * wsp2[1] - wsp2[0] * wsp1[1]))
            punkt_przec = Punkt(px, py)
            return punkt_przec

    def trojkat_z_prostych(self, wsp1, wsp2, wsp3):
        p1 = self.trojkat_wspolcznniki_spr(wsp1, wsp2)
        p2 = self.trojkat_wspolcznniki_spr(wsp2, wsp3)
        p3 = self.trojkat_wspolcznniki_spr(wsp1, wsp3)
        if p1 is not None and p2 is not None and p3 is not None:
            self.t1 = p1
            self.t2 = p2
            self.t3 = p3