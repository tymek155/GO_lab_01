import copy
import Punkt, Wektor
from Wektor import Wektor
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
        wspolczynnik_b = (self.pkt_1.y * self.pkt_2.x - self.pkt_2.y * self.pkt_1.x) / (self.pkt_2.x - self.pkt_1.x)
        return wspolczynnik_a, wspolczynnik_b

    def sprawdz_przynaleznosc_prosta(self, spr: type[Punkt]):
        wspolczynnik_a, wspolczynnik_b = self.rownanie_prostej()
        if (wspolczynnik_a * spr.x + wspolczynnik_b) == spr.y:
            return True
        else:
            return False

    def sprawdz_przynaleznosc_odcinek(self, spr: type[Punkt]):
        if spr.x <= self.pkt_2.x and spr.x >= self.pkt_1.x:
            return self.sprawdz_przynaleznosc_prosta(spr)
        else:
            return False

    def polozenie_pkt_prosta(self, spr: type[Punkt]):
        wspolczynnik_a, wspolczynnik_b = self.rownanie_prostej()
        y_prosta = wspolczynnik_a * spr.x + wspolczynnik_b
        if y_prosta <= spr.y + 0.001 and y_prosta >= spr.y - 0.001:
            print("Punkt leży na prostej.")
            return 2
        elif spr.y > y_prosta:
            print("Punkt leży po prawej stronie.")
            return 1
        else:
            print("Punkt leży po lewej stronie.")
            return 3

    def translacja_linii(self, wektor: type[Wektor]):
        wektor_copy = copy.deepcopy(wektor)
        self.pkt_1.x = self.pkt_1.x + (wektor.pkt_2.x - wektor.pkt_1.x)
        self.pkt_2.x = self.pkt_2.x + (wektor_copy.pkt_2.x - wektor_copy.pkt_1.x)

        self.pkt_1.y = self.pkt_1.y + (wektor.pkt_2.y - wektor.pkt_1.y)
        self.pkt_2.y = self.pkt_2.y + (wektor_copy.pkt_2.y - wektor_copy.pkt_1.y)

    def odbicie_punktu_linia(self, punkt: type[Punkt]):
        A, C = self.rownanie_prostej()
        B = -1

        opt = self.polozenie_pkt_prosta(punkt)
        if opt == 3:
            wek_x = -A
            wek_y = -B
        elif opt == 1:
            wek_x = A
            wek_y = B
        else:
            print("Błąd, punkt na prostej")
            return None

        odleglosc = (abs(A * punkt.x + B * punkt.y + C)) / (math.sqrt(A * A + B * B))

        t = odleglosc / (math.sqrt(wek_x * wek_x + wek_y * wek_y))

        wek_x *= t
        wek_y *= t

        wek_x = 2 * wek_x
        wek_y = 2 * wek_y

        x_odb = wek_x + punkt.x
        y_odb = wek_y + punkt.y

        punkt_odb = Punkt
        punkt_odb.x = x_odb
        punkt_odb.y = y_odb

        wektor_w = Wektor(punkt, punkt_odb)

        return wektor_w
