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
