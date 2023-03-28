def is_palindrom_loop(tekst: str) -> bool:
    n = len(tekst)
    tekst = tekst.lower()
    for index in range(int(n / 2)):  # n // 2
        # jezeli odpowiadacy element od tyłu nie jest rowne temu z przodu - tekst nie jest palindromem
        if tekst[index] != tekst[n - 1 - index]:
            return False
    return True


def is_palindrom_str(tekst: str) -> bool:
    tekst = tekst.lower()
    return tekst == tekst[::-1]


print(is_palindrom_loop('Kajak'))  # True
print(is_palindrom_loop('Kawa'))  # False
print(is_palindrom_str('Kajak'))  # True
print(is_palindrom_str('Kawa'))  # False


def oblicz_suma_z_dicta(dictionary: dict) -> int:
    suma = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            suma += value
    return suma


d = {'a': 100, 'b': 200, 'c': 500, 'd': 'tekst','e': '800'}
print(oblicz_suma_z_dicta(d))  # 800


def is_palindrom(tekst: str) -> bool:
  tekst = tekst.lower()
  a=0 #licznik obrotów
  while a in range(len(tekst)//2):
    pierwsza_litera = tekst[a]
    ost_litera = tekst[len(tekst) - 1 - a]
    if pierwsza_litera != ost_litera:
      return False
    else:
      a+=1
  return True

print(is_palindrom('Kajak'))  # True
print(is_palindrom('Kawa'))  # False

class MojaKlasa:
# https://stackoverflow.com/questions/11769020/is-it-possible-to-override-name-derived-from-object
    def __init__(self):
        self.__class__.__name__ = 'inna nazwa'



klasa = MojaKlasa
print(klasa.__name__)