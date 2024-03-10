import Show
from Punkt import Punkt
from Linia import Linia
import tkinter as tk
from tkinter import simpledialog

def dodaj_punkt(baza_pkt):
    pkt = Punkt
    pkt.x = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną x:")
    pkt.y = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną y:")
    baza_pkt.append(pkt)
    Show.wyswietl_punkt(pkt.x, pkt.y)

def dodaj_linie(baza_lin):
    pkt1 = Punkt(0,0)
    pkt1.x = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną x1:")
    pkt1.y = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną y1:")

    pkt2 = Punkt(0,0)
    pkt2.x = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną x2:")
    pkt2.y = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną y2:")

    linia = Linia(pkt1,pkt2)
    baza_lin.append(linia)
    Show.wyswietl_linie(pkt1.x,pkt1.y,pkt2.x,pkt2.y)

def dodaj_wektor(baza_wek):
    wek1 = Punkt(0,0)
    wek2 = Punkt(0,0)

    wek1.x = simpledialog.askfloat("Dodaj wektor", "Podaj współrzędną x1:")
    wek1.y = simpledialog.askfloat("Dodaj wektor", "Podaj współrzędną y1:")

    wek2.x = simpledialog.askfloat("Dodaj wektor", "Podaj współrzędną x2:")
    wek2.y = simpledialog.askfloat("Dodaj wektor", "Podaj współrzędną y2:")

    wek = Linia(wek1,wek2)
    baza_wek.append(wek)
    Show.wyswietl_wektor(wek1.x, wek1.y, wek2.x, wek2.y)

#def wybierz_punkt(baza_punkt, okno):
   # for punkt in baza_punkt:
       # b_pkt =  tk.Button(okno, text=f"Punkkt x: {}")
'''
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
okno = tk.Tk()
    okno.title("Funkcje dla punktów i linii")
    baza_pkt = []
    baza_lin = []
    baza_wek = []

    ramka_pkt = tk.Frame(okno)
    ramka_pkt.pack(padx=100)

    b_dodaj_punkt = tk.Button(okno, text="Dodaj punkt do bazy", command= lambda:Input.dodaj_punkt(baza_pkt))
    b_dodaj_punkt.pack(pady=20)

    b_dodaj_lin = tk.Button(okno, text="Dodaj linię do bazy", command=lambda:Input.dodaj_linie(baza_lin))
    b_dodaj_lin.pack(pady=20)

    b_dodaj_wek = tk.Button(okno, text="Dodaj wektor do bazy", command=lambda:Input.dodaj_wektor(baza_wek))
    b_dodaj_wek.pack(pady=20)

    b_




        #print("4. Wylicz równanie prostej dla danej linii.")
        #print("5. Sprawdz przynależność punktu do prostej.")
        #print("6. Sprawdź przynależność punktu do linii (odcinka).")
        #print("7. Sprawdź położenie punktu względem prostej.")
        #print("8. Wykonaj translacje linii o wybrany wektor.")
        #print("9. Odbij punkt względem linii.")
    okno.mainloop()'''