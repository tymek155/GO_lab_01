import Punkt
import math

from Linia import Linia
from Punkt import Punkt
from Punkt import k_fun_y

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

    def pole_trojkata(self):
        bok_a = self.t1.oblicz_dlugosc(self.t2)
        bok_b = self.t2.oblicz_dlugosc(self.t3)
        bok_c = self.t3.oblicz_dlugosc(self.t1)
        p = (bok_a + bok_b + bok_c)/2

        return math.sqrt(p*(p-bok_a)*(p-bok_b)*(p-bok_c))

    def przynaleznosc_punktu_pole(self, punkt: type[Punkt]):
        pole_bazowe = self.pole_trojkata()

        trojkat_s1 = Trojkat(self.t1, self.t2, punkt)
        trojkat_s2 = Trojkat(self.t2, self.t3, punkt)
        trojkat_s3 = Trojkat(self.t3, self.t1, punkt)

        s1 = trojkat_s1.pole_trojkata()
        s2 = trojkat_s2.pole_trojkata()
        s3 = trojkat_s3.pole_trojkata()

        if pole_bazowe >= (s1 + s2 + s3):
            return True
        else:
            return False

    def przynaleznosc_punktu_strona(self, punkt: type[Punkt]):
        punkty = [self.t1, self.t2, self.t3]
        punkty_sort = sorted(punkty, key=k_fun_y)
        linia1 = Linia(punkty_sort[0], punkty_sort[1])
        linia2 = Linia(punkty_sort[1], punkty_sort[2])
        linia3 = Linia(punkty_sort[2], punkty_sort[0])
        linie = [linia1, linia2, linia3]

        for i in linie:
            if i.polozenie_pkt_prosta(punkt) == 2:
                if i.sprawdz_przynaleznosc_odcinek(punkt) == True:
                    return True

        if punkty_sort[2].y == punkty_sort[1].y:
            if linia2.polozenie_pkt_prosta(punkt) == 1 and ((linia1.polozenie_pkt_prosta(punkt) == 1 and linia3.polozenie_pkt_prosta(punkt) == 3) or (linia1.polozenie_pkt_prosta(punkt) == 3 and linia3.polozenie_pkt_prosta(punkt) == 1)):
                return True
            else:
                return False
        else:
            if linia2.polozenie_pkt_prosta(punkt) == 1 and linia3.polozenie_pkt_prosta(punkt) == 1 and linia1.polozenie_pkt_prosta(punkt) == 3:
                return True
            else:
                return False