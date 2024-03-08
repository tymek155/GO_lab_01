import Punkt, Linia, Input
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def main():
    okno = tk.Tk()
    okno.title("Funkcje dla punktów i linii")
    baza_pkt = []
    baza_lin = []
    baza_wek = []
    b_dodaj_punkt = tk.Button(okno, text="Dodaj punkt do bazy", command= lambda:Input.dodaj_punkt(baza_pkt))
    b_dodaj_punkt.pack()

    b_dodaj_lin = tk.Button(okno, text="Dodaj linię do bazy", command=lambda:Input.dodaj_linie(baza_lin))
    b_dodaj_lin.pack()

    b_dodaj_wek = tk.Button(okno, text="Dodaj wektor do bazy", command=lambda:Input.dodaj_wektor(baza_wek))
    b_dodaj_wek.pack()



        #print("3. Dodaj wektor do bazy.")
        #print("4. Wylicz równanie prostej dla danej linii.")
        #print("5. Sprawdz przynależność punktu do prostej.")
        #print("6. Sprawdź przynależność punktu do linii (odcinka).")
        #print("7. Sprawdź położenie punktu względem prostej.")
        #print("8. Wykonaj translacje linii o wybrany wektor.")
        #print("9. Odbij punkt względem linii.")
    okno.mainloop()




if __name__ == '__main__':
    main()


