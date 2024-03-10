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
    punkt6 = Punkt(1,1)
    punkt7 = Punkt(-2,-1)
    linia = Linia(punkt1, punkt2)
    wektor = Wektor(punkt1, punkt7)

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


if __name__ == '__main__':
    main()


