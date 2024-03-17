import copy
import math

from matplotlib import pyplot as plt

import Punkt
import Wektor
from Punkt import Punkt
from Wektor import Wektor


class Linia:
    def __init__(self, a: type[Punkt], b: type[Punkt]):
        if a.x < b.x:
            self.pkt_1 = a
            self.pkt_2 = b
        else:
            self.pkt_1 = b
            self.pkt_2 = a

    def rownanie_prostej(self):
        if self.pkt_1.x == self.pkt_2.x:
            return 0, 0
        wspolczynnik_a = (self.pkt_1.y - self.pkt_2.y) / (self.pkt_1.x - self.pkt_2.x)
        wspolczynnik_b = (self.pkt_1.y * self.pkt_2.x - self.pkt_2.y * self.pkt_1.x) / (self.pkt_2.x - self.pkt_1.x)
        return wspolczynnik_a, wspolczynnik_b

    def rownanie_ogolne(self):
        if self.pkt_1.x == self.pkt_2.x:
            return 1, 0, (-self.pkt_1.x)
        else:
            A,C = self.rownanie_prostej()
            B = -1
            return A,B,C

    def sprawdz_przynaleznosc_prosta(self, spr: type[Punkt]):
        wspolczynnik_a, wspolczynnik_b = self.rownanie_prostej()
        if wspolczynnik_a == 0 and wspolczynnik_b == 0:
            if self.pkt_1.x == spr.x:
                return True
            else:
                return False
        else:
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
        if wspolczynnik_a == 0 and wspolczynnik_b == 0:
            if self.pkt_1.x == spr.x:
                print("Punkt leży na prostej.")
                return 2
            elif self.pkt_1.x < spr.x:
                print("Punkt leży po prawej stronie.")
                return 1
            else:
                print("Punkt leży po lewej stronie.")
                return 3

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

        if A == 0 and C == 0:
            punkt_odb = Punkt
            odleglosc = abs(self.pkt_1.x - punkt.x)
            punkt_odb.y = punkt.y
            punkt_odb.x = self.pkt_1.x + odleglosc
            wektor_w = Wektor(punkt, punkt_odb)
            plt.xlim(-4 * odleglosc, 4 * odleglosc)
            plt.ylim(-4 * odleglosc, 4 * odleglosc)
            return wektor_w

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
        plt.xlim(-4*odleglosc, 4*odleglosc)
        plt.ylim(-4*odleglosc, 4*odleglosc)
        return wektor_w

    def przeciecie_prostych(self, prosta2):
        A1, B1, C1 = self.rownanie_ogolne()
        A2, B2, C2 = prosta2.rownanie_ogolne()
        if(A1*B2 - A2*B1) == 0:
            print("Proste rownolegle!")
            return None
        else:
            px = ((C2*B1-C1*B2)/(A1*B2 - A2*B1))
            py = ((A2*C1-A1*C2)/(A1*B2 - A2*B1))
            punkt_przec = Punkt(px, py)
            return punkt_przec

    def przeciecie_linii(self, linia2):
        punkt = self.przeciecie_prostych(linia2)
        if(punkt != None):
            if punkt.x >= self.pkt_1.x and punkt.x <= self.pkt_2.x and punkt.y >= self.pkt_1.y and punkt.y <= self.pkt_2.y:
                if punkt.x >= linia2.pkt_1.x and punkt.x <= linia2.pkt_2.x and punkt.y >= linia2.pkt_1.y and punkt.y <= linia2.pkt_2.y:
                    print("Punkt lezy na przecieciu linii!")
                    return True
        return False

    def punkt_prosta_odlg(self, punkt):
        A,B, C = self.rownanie_ogolne()
        opt = self.polozenie_pkt_prosta(punkt)
        if B == 0:
            odleglosc = abs(self.pkt_1.x - punkt.x)
            print(f"Odleglosc miedzy punktami wynosi: {odleglosc}")
            if opt == 3:
                p_odl = Punkt(punkt.x + odleglosc, punkt.y)
            elif opt == 1:
                p_odl = Punkt(punkt.x - odleglosc, punkt.y)
            else:
                print("Błąd, punkt na prostej")
                return None,0
            linia = Linia(punkt, p_odl)
            return linia, odleglosc

        odleglosc = (abs(A * punkt.x + B * punkt.y + C)) / (math.sqrt(A * A + B * B))

        if opt == 3:
            lin_x = -A
            lin_y = -B
        elif opt == 1:
            lin_x = A
            lin_y = B
        else:
            print("Błąd, punkt na prostej")
            return None,0

        t = odleglosc / (math.sqrt(lin_x * lin_x + lin_y * lin_y))
        print(f"Odleglosc miedzy punktami wynosi: {odleglosc}")

        lin_x *= t
        lin_y *= t

        x_lin = lin_x + punkt.x
        y_lin = lin_y + punkt.y

        punkt_lin = Punkt
        punkt_lin.x = x_lin
        punkt_lin.y = y_lin

        linia_laczaca = Linia(punkt, punkt_lin)
        return linia_laczaca, odleglosc