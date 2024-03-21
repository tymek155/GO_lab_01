import matplotlib.pyplot as plt
from Linia import Linia

def powrot_do_menu():
    print("Powrót do menu")

def wyswietl_punkt(punkt):
    plt.scatter(punkt.x, punkt.y, color="blue")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_linie_short(linia):
    plt.plot([linia.pkt_1.x, linia.pkt_2.x], [linia.pkt_1.y, linia.pkt_2.y], color="red")
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

def wyswietl_linie(linia):
    plt.plot([linia.pkt_1.x, linia.pkt_2.x], [linia.pkt_1.y, linia.pkt_2.y], color="red")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_wektor_short(wektor):
    plt.arrow(wektor.pkt_1.x, wektor.pkt_1.y, wektor.pkt_2.x - wektor.pkt_1.x, wektor.pkt_2.y - wektor.pkt_1.y, head_width=0.1,head_length=0.1, color="orange")

def wyswietl_wektor(wektor):
    plt.arrow(wektor.pkt_1.x, wektor.pkt_1.y, wektor.pkt_2.x - wektor.pkt_1.x, wektor.pkt_2.y - wektor.pkt_1.y, head_width=0.1,head_length=0.1, color="orange")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_prosta_short(linia):
    xmi = -100
    xma = 100
    x = [xmi,xma]
    a,b = linia.rownanie_prostej()
    if a== 0 and b == 0:
        x = [linia.pkt_1.x, linia.pkt_2.x]
        y = [xmi, xma]
    else:
        y = [a * xmi + b, a * xma + b]
    plt.axis("equal")
    plt.plot(x,y, color="pink")

def wyswietl_prosta(linia):
    xmi = -100
    xma = 100
    x = [xmi,xma]
    a,b = linia.rownanie_prostej()
    if a== 0 and b == 0:
        x = [linia.pkt_1.x, linia.pkt_2.x]
        y = [xmi, xma]
    else:
        y = [a * xmi + b, a * xma + b]
    plt.plot(x,y, color="green")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_prosta_punkt(linia, punkt, spr):
    xmi = -50
    xma = 50
    x = [xmi, xma]
    a, b = linia.rownanie_prostej()
    y = [a * xmi + b, a * xma + b]
    plt.plot(x, y, color="green")
    plt.scatter(punkt.x, punkt.y, color="blue")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    if spr == True:
        plt.text(punkt.x + 0.25, punkt.y + 0.1*abs(punkt.y), "Punkt znajduje się na prostej", horizontalalignment="center")
    else:
        plt.text(punkt.x + 0.25, punkt.y + 0.1*abs(punkt.y), "Punkt nie znajduje się na prostej", horizontalalignment="center")
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_linia_punkt(linia, punkt, spr):
    plt.plot([linia.pkt_1.x, linia.pkt_2.x], [linia.pkt_1.y, linia.pkt_2.y], color="red")
    plt.scatter(punkt.x, punkt.y, color="blue")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    if spr == True:
        plt.text(punkt.x + 0.25, punkt.y + 0.1, "Punkt znajduje się na linii", horizontalalignment="center")
    else:
        plt.text(punkt.x + 0.25, punkt.y + 0.1, "Punkt nie znajduje się na linii", horizontalalignment="center")
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_polozenie_pkt_prosta(linia, punkt, spr):
    xmi = -50
    xma = 50
    x = [xmi, xma]
    a, b = linia.rownanie_prostej()
    if a== 0 and b == 0:
        x = [linia.pkt_1.x, linia.pkt_2.x]
        y = [xmi, xma]
    else:
        y = [a * xmi + b, a * xma + b]

    plt.plot(x, y, color="green")
    plt.scatter(punkt.x, punkt.y, color="blue")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)

    if spr == 1:
        plt.text(punkt.x + 0.25, punkt.y + 0.1, "Punkt znajduje się po prawej stronie prostej", horizontalalignment="center")
    elif spr == 2:
        plt.text(punkt.x + 0.25, punkt.y + 0.1, "Punkt znajduje się na prostej", horizontalalignment="center")
    else:
        plt.text(punkt.x + 0.25, punkt.y + 0.1, "Punkt znajduje się po lewej stronie prostej", horizontalalignment="center")
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_translacja(linia, wektor):
    wyswietl_prosta_short(linia)
    wyswietl_wektor_short(wektor)
    linia.translacja_linii(wektor)
    wyswietl_prosta(linia)

def wyswietl_odb_pkt(punkt, linia):
    plt.scatter(punkt.x, punkt.y, s=1, color="blue")
    wektor = linia.odbicie_punktu_linia(punkt)
    if wektor is None:
        return None
    wyswietl_wektor_short(wektor)
    plt.scatter(wektor.pkt_2.x, wektor.pkt_2.y, s=1, color="blue")
    wyswietl_prosta(linia)

def wyswietl_przeciecie_prostych(prosta1, prosta2):
    wyswietl_prosta_short(prosta1)
    punkt_przeciecia = prosta1.przeciecie_prostych(prosta2)
    if punkt_przeciecia == None:
        plt.axis('square')
        plt.xlim(prosta1.pkt_1.x- 5*abs(prosta1.pkt_1.x), prosta1.pkt_1.x+5*abs(prosta1.pkt_1.x))
        plt.ylim(prosta1.pkt_1.y - 5*abs(prosta1.pkt_1.y), prosta1.pkt_1.y + 5*abs(prosta1.pkt_1.y))
        wyswietl_prosta(prosta2)
    else:
        wyswietl_prosta_short(prosta2)
        #plt.axis('square')
        plt.xlim(prosta1.pkt_1.x - 5 * abs(prosta1.pkt_1.x), prosta1.pkt_1.x + 5 * abs(prosta1.pkt_1.x))
        plt.ylim(prosta1.pkt_1.y - 5 * abs(prosta1.pkt_1.y), prosta1.pkt_1.y + 5 * abs(prosta1.pkt_1.y))
        wyswietl_punkt(punkt_przeciecia)

def wyswietl_przeciecie_linii(linia1, linia2):
    wyswietl_linie_short(linia1)
    punkt_przeciecia = linia1.przeciecie_prostych(linia2)
    if linia1.przeciecie_linii(linia2) == True:
        wyswietl_linie_short(linia2)
        plt.xlim(linia1.pkt_1.x - 5*abs(linia1.pkt_1.x), linia1.pkt_1.x + 5*abs(linia1.pkt_1.x))
        plt.ylim(linia1.pkt_1.y - 5*abs(linia1.pkt_1.y), linia1.pkt_1.y + 5*abs(linia1.pkt_1.y))
        wyswietl_punkt(punkt_przeciecia)
    else:
        plt.xlim(linia1.pkt_1.x - 5*abs(linia1.pkt_1.x), linia1.pkt_1.x + 5*abs(linia1.pkt_1.x))
        plt.ylim(linia1.pkt_1.y - 5*abs(linia1.pkt_1.y), linia1.pkt_1.y + 5*abs(linia1.pkt_1.y))
        wyswietl_linie(linia2)

def wyswietl_punkt_prosta_odleglosc(punkt, prosta):
    wyswietl_prosta_short(prosta)
    linia, odleglosc = prosta.punkt_prosta_odlg(punkt)
    if linia is not None:
        wyswietl_linie_short(linia)
    #if odleglosc != 0:
        #plt.xlim(punkt.x - 5*odleglosc, punkt.x +5*odleglosc)
        #plt.xlim(punkt.y - 5 * odleglosc, punkt.y + 5 * odleglosc)
    #else:
        #plt.xlim(punkt.x - 5 * punkt.x , punkt.x + 5 * punkt.x )
        #plt.xlim(punkt.y - 5 * punkt.y, punkt.y + 5 * punkt.y)
    plt.axis('square')
    wyswietl_punkt(punkt)

def wyswietl_trojkat(trojkat):
    x = [trojkat.t1.x, trojkat.t2.x, trojkat.t3.x, trojkat.t1.x]
    y = [trojkat.t1.y, trojkat.t2.y, trojkat.t3.y, trojkat.t1.y]
    plt.plot(x, y, 'b')
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    pole = trojkat.pole_trojkata()
    round(pole, 1)
    plt.text(trojkat.t1.x, trojkat.t1.y + 0.1, "Pole trojkata wynosi: " + str(round(pole,4)), fontweight = "bold", color = "blue")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.axis('square')
    plt.show()

def wyswietl_pole_linii(linia1, linia2, linia3):
    wyswietl_linie_short(linia1)
    wyswietl_linie_short(linia2)
    wyswietl_linie_short(linia3)
    pole = linia1.pole_trzy_linie(linia2, linia3)
    if pole == None:
        plt.text(linia1.pkt_1.x, linia1.pkt_1.y +0.1, "Linie nie przecinaja się! ", fontweight = "bold", color = "blue")
    else:
        plt.text(linia1.pkt_1.x, linia1.pkt_1.y + 0.1, "Pole wynosi: " + str(round(pole,4)), fontweight = "bold", color = "blue")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.axis('equal')
    plt.show()

def wyswietl_przynaleznosc_punktu_pole(trojkat, punkt):
     wyswietl_linie_short(Linia(punkt, trojkat.t1))
     wyswietl_linie_short(Linia(punkt, trojkat.t2))
     wyswietl_linie_short(Linia(punkt, trojkat.t3))
     plt.scatter(punkt.x, punkt.y, color="blue")
     opt = trojkat.przynaleznosc_punktu_pole(punkt)
     if opt == True:
         plt.text(trojkat.t2.x, trojkat.t2.y + 0.1, "Punkt należy do trójkąta!", fontweight="bold", color="orange")
     else:
         plt.text(trojkat.t2.x, trojkat.t2.y + 0.1, "Punkt nie należy do trójkąta!", fontweight="bold", color="orange")

     plt.axis('square')
     wyswietl_trojkat(trojkat)


def wyswietl_przynaleznosc_punktu_strona(trojkat, punkt):
    wyswietl_linie_short(Linia(punkt, trojkat.t1))
    wyswietl_linie_short(Linia(punkt, trojkat.t2))
    wyswietl_linie_short(Linia(punkt, trojkat.t3))
    plt.scatter(punkt.x, punkt.y, color="blue")
    opt = trojkat.przynaleznosc_punktu_strona(punkt)
    if opt == True:
        plt.text(trojkat.t2.x, trojkat.t2.y + 0.1, "Punkt należy do trójkąta!", fontweight="bold", color="orange")
    else:
        plt.text(trojkat.t2.x, trojkat.t2.y + 0.1, "Punkt nie należy do trójkąta!", fontweight="bold", color="orange")

    plt.axis('square')
    wyswietl_trojkat(trojkat)

def wyswietl_wielokat(wielokat):
    if wielokat.sprawdz_przeciecia() == False:
        return None
    for i in range(0, len(wielokat.punkty) -1):
        wyswietl_linie_short(Linia(wielokat.punkty[i], wielokat.punkty[i+1]))
    plt.axis('square')
    wyswietl_linie(Linia(wielokat.punkty[0], wielokat.punkty[len(wielokat.punkty)-1]))
