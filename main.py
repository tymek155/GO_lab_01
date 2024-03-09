import Show
from Punkt import Punkt
from Linia import Linia
from Wektor import Wektor

def main():
    punkt1 = Punkt(2,2)
    punkt2 = Punkt(4,4)
    punkt3 = Punkt(-20,-10)
    punkt4 = Punkt(10, -10)
    punkt5 = Punkt(10, 15)
    linia = Linia(punkt1, punkt2)
    wektor = Wektor(punkt1, punkt3)

    #Show.wyswietl_punkt(punkt1)

    #Show.wyswietl_linie(linia)

    #Show.wyswietl_wektor(wektor)

    #Show.wyswietl_prosta(linia)

    #Show.wyswietl_prosta_punkt(linia, punkt3, linia.sprawdz_przynaleznosc_prosta(punkt3))
    #Show.wyswietl_prosta_punkt(linia, punkt1, linia.sprawdz_przynaleznosc_prosta(punkt1))

    #Show.wyswietl_linia_punkt(linia, punkt3, linia.sprawdz_przynaleznosc_odcinek(punkt3))
    #Show.wyswietl_linia_punkt(linia, punkt1, linia.sprawdz_przynaleznosc_odcinek(punkt2))

    #Show.wyswietl_polozenie_pkt_prosta(linia, punkt3, linia.polozenie_pkt_prosta(punkt3))
    #Show.wyswietl_polozenie_pkt_prosta(linia, punkt4, linia.polozenie_pkt_prosta(punkt4))
    #Show.wyswietl_polozenie_pkt_prosta(linia, punkt5, linia.polozenie_pkt_prosta(punkt5))

    #Show.wyswietl_translacja(linia, wektor)

    Show.wyswietl_odb_pkt(punkt3, linia)


if __name__ == '__main__':
    main()









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