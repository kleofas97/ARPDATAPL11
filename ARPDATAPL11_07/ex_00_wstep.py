# debugging - mozna krok po kroku wykonywac program z dostepem do zmiennych 'live'

# mozliwosci importowania modulow lokalnych
import ARPDATAPL11_07.utils as utils # zalecany
# from ARPDATAPL11_07.utils import sum_two_number # niezalecany zapis
# import ARPDATAPL11_07.utils   # za dlugi lepiej opcja 1

# utils.sum_two_number jest mozliwe do uzycia, poniwaz pobralem modul utils w linijce 2
wynik = utils.sum_two_number(5,6)
print(wynik)


# __name__ == __main__ oznacza wykonanie programu wewnatrz poniższego if'a tylko wtedy
# gdy uruchamiamy ten wlasnie plik (a nie np. importujemy go do innego pliku)
if __name__ == "__main__":
    print('Jestem w __main__ ex 00')
