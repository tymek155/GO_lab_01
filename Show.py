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
    plt.show()

def wyswietl_linie(linia):
    plt.plot([linia.pkt_1.x, linia.pkt_2.x], [linia.pkt_1.y, linia.pkt_2.y], color="red")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    plt.show()

def wyswietl_wektor_short(wektor):
    plt.arrow(wektor.pkt_1.x, wektor.pkt_1.y, wektor.pkt_2.x - wektor.pkt_1.x, wektor.pkt_2.y - wektor.pkt_1.y, head_width=0.1,head_length=0.1, color="orange")

def wyswietl_wektor(wektor):
    plt.arrow(wektor.pkt_1.x, wektor.pkt_1.y, wektor.pkt_2.x - wektor.pkt_1.x, wektor.pkt_2.y - wektor.pkt_1.y, head_width=0.1,head_length=0.1, color="orange")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    plt.show()

def wyswietl_prosta_short(linia):
    xmi = -100
    xma = 100
    x = [xmi,xma]
    a,b = linia.rownanie_prostej()
    y = [a*xmi +b, a*xma + b]
    plt.plot(x,y, color="pink")

def wyswietl_prosta(linia):
    xmi = -100
    xma = 100
    x = [xmi,xma]
    a,b = linia.rownanie_prostej()
    y = [a*xmi +b, a*xma + b]
    plt.plot(x,y, color="green")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    plt.show()

def wyswietl_prosta_punkt(linia, punkt, spr):
    xmi = -100
    xma = 100
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
        plt.text(punkt.x + 0.25, punkt.y + 0.1, "Punkt znajduje się na prostej", horizontalalignment="center")
    else:
        plt.text(punkt.x + 0.25, punkt.y + 0.1, "Punkt nie znajduje się na prostej", horizontalalignment="center")
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
    plt.show()

def wyswietl_polozenie_pkt_prosta(linia, punkt, spr):
    xmi = -100
    xma = 100
    x = [xmi, xma]
    a, b = linia.rownanie_prostej()
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

    plt.show()

def wyswietl_translacja(linia, wektor):
    wyswietl_prosta_short(linia)
    wyswietl_wektor_short(wektor)
    linia.translacja_linii(wektor)
    wyswietl_prosta(linia)
    '''
        
    '''