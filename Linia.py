import copy

import Punkt, Wektor
import math

class Linia:
    def __init__(self, a: type[Punkt], b: type[Punkt]):
        if a.x < b.x:
            self.pkt_1 = a
            self.pkt_2 = b
        else:
            self.pkt_1 = b
            self.pkt_2 = a

    def rownanie_prostej(self):
        wspolczynnik_a = (self.pkt_1.y - self.pkt_2.y) / (self.pkt_1.x - self.pkt_2.x)
        wspolczynnik_b = (self.pkt_1.y*self.pkt_2.x-self.pkt_2.y*self.pkt_1.x)/(self.pkt_2.x-self.pkt_1.x)
        return wspolczynnik_a, wspolczynnik_b

    def sprawdz_przynaleznosc_prosta(self, spr: type[Punkt]):
        wspolczynnik_a, wspolczynnik_b = self.rownanie_prostej()
        if (wspolczynnik_a * spr.x + wspolczynnik_b) == spr.y:
            return True
        else:
            return False

    def sprawdz_przynaleznosc_odcinek(self, spr: type[Punkt]):
        if spr.x <= self.pkt_2.x and spr.x>= self.pkt_1.x:
            return self.sprawdz_przynaleznosc_prosta(spr)
        else:
            return False

    def polozenie_pkt_prosta(self, spr: type[Punkt]):
        wspolczynnik_a, wspolczynnik_b = self.rownanie_prostej()
        y_prosta = wspolczynnik_a*spr.x + wspolczynnik_b
        if spr.y > y_prosta:
            print("Punkt leży po prawej stronie.")
            return 1
        elif spr.y == y_prosta:
            print("Punkt leży na prostej.")
            return 2
        else:
            print("Punkt leży po lewej stronie.")
            return 3

    def translacja_linii(self, wektor : type[Wektor]):
        wektor_copy = copy.deepcopy(wektor)
        self.pkt_1.x = self.pkt_1.x + (wektor.pkt_2.x - wektor.pkt_1.x)
        self.pkt_2.x = self.pkt_2.x + (wektor_copy.pkt_2.x - wektor.pkt_1.x)

        self.pkt_1.y = self.pkt_1.y + (wektor.pkt_2.y - wektor.pkt_1.y)
        self.pkt_2.y = self.pkt_2.y + (wektor_copy.pkt_2.y - wektor.pkt_1.y)

    def odbicie_punktu_linia(self, punkt:type [Punkt]):
        A, C = self.rownanie_prostej()
        B = -1
        odleglosc = (abs(A*punkt.x + B*punkt.y + C))/(math.sqrt(A*A+B*B))
        wektor = Punkt(punkt.x, punkt.y)

        wektor.x = -wektor.x * odleglosc
        wektor.y = -wektor.y * odleglosc

        xp = punkt.x
        yp = punkt.y

        punkt.x = wektor.x + xp
        punkt.y = wektor.y + yp


