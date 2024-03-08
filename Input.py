import Punkt, Linia
import tkinter as tk
from tkinter import simpledialog

def dodaj_punkt(baza_pkt):
    pkt = Punkt
    pkt.x = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną x:")
    pkt.y = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną y:")
    baza_pkt.append(pkt)

def dodaj_linie(baza_lin):
    pkt1 = Punkt
    pkt1.x = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną x1:")
    pkt1.y = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną y1:")

    pkt2 = Punkt
    pkt2.x = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną x2:")
    pkt2.y = simpledialog.askfloat("Dodaj punkt", "Podaj współrzędną y2:")

    baza_lin.append(Linia(pkt1, pkt2))

def dodaj_wektor(baza_wek):
    wek = Punkt
    wek.x = simpledialog.askfloat("Dodaj wektor", "Podaj współrzędną x:")
    wek.y = simpledialog.askfloat("Dodaj wektor", "Podaj współrzędną y:")
    baza_wek.append(wek)

def wybierz_punkt(baza_punkt, okno):
    for punkt in baza_punkt:
        b_pkt =  tk.Button(okno, text=f"Punkkt x: {}")
