import Show
from Trojkat import Trojkat
from Punkt import Punkt
from Linia import Linia
from Wektor import Wektor

def main():



    #Show.wyswietl_punkt(punkt1)

    #Show.wyswietl_linie(linia)

    #Show.wyswietl_wektor(wektor)

    #Show.wyswietl_prosta(linia)

    #Show.wyswietl_prosta_punkt(linia, punkt3, linia.sprawdz_przynaleznosc_prosta(punkt3))
    #Show.wyswietl_prosta_punkt(linia, punkt1, linia.sprawdz_przynaleznosc_prosta(punkt1))

    #Show.wyswietl_linia_punkt(linia, punkt6, linia.sprawdz_przynaleznosc_odcinek(punkt3))
    #Show.wyswietl_linia_punkt(linia, punkt1, linia.sprawdz_przynaleznosc_odcinek(punkt2))

    #Show.wyswietl_polozenie_pkt_prosta(linia, punkt3, linia.polozenie_pkt_prosta(punkt3))
    #Show.wyswietl_polozenie_pkt_prosta(linia, punkt2, linia.polozenie_pkt_prosta(punkt2))
    #Show.wyswietl_polozenie_pkt_prosta(linia, punkt4, linia.polozenie_pkt_prosta(punkt4))

    #Show.wyswietl_translacja(linia, wektor)

    #Show.wyswietl_odb_pkt(punkt3, linia)

    punkt1 = Punkt(3,10)
    punkt2 = Punkt(3, 3)
    linia1 = Linia(punkt1, punkt2)
    punkt3 = Punkt(0,0)
    punkt4 = Punkt(4,2)
    linia2 = Linia(punkt3, punkt4)
    punkt5 = Punkt(0,3)
    linia3 = Linia(punkt3, punkt5)
    Show.wyswietl_przeciecie_prostych(linia1, linia2)
    Show.wyswietl_przeciecie_prostych(linia1, linia3)

    punkt6 = Punkt(5,7)
    linia4 = Linia(punkt2, punkt6)
    Show.wyswietl_przeciecie_linii(linia1, linia2)
    Show.wyswietl_przeciecie_linii(linia1, linia4)

    punkt7= Punkt(12, 10)
    Show.wyswietl_punkt_prosta_odleglosc(punkt7, linia1)
    Show.wyswietl_punkt_prosta_odleglosc(punkt6, linia2)

    trojkat1 = Trojkat(punkt1, punkt2, punkt3)
    Show.wyswietl_trojkat(trojkat1)
    trojkat1.trojkat_z_prostych([1, -1, 3], [2, -1, 4], [0.5, -1, 5])
    Show.wyswietl_trojkat(trojkat1)

if __name__ == '__main__':
    main()


