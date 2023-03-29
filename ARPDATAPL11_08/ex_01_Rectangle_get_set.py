# napisz klase Rectangle
# parametry bok1, bok2 (jako property) <-- gettery settery wraz z ochrona przed wpisaniem glupot
# metody get area oraz get diagonal
import math

class Rectangle:

    def __init__(self, bok1, bok2):
        self._bok1 = bok1
        self._bok2 = bok2

    @property
    def bok1(self):
        return self._bok1

    @bok1.setter
    def bok1(self,new_bok):
        if isinstance(new_bok, (int,float)):
            self._bok1 = new_bok
        else:
            print('Zla wartosc - bok1 niezmieniony')

    @property
    def bok2(self):
        return self._bok1

    @bok2.setter
    def bok2(self, new_bok):
        if isinstance(new_bok, (int, float)):
            self._bok2 = new_bok
        else:
            print('Zla wartosc - bok1 niezmieniony')

    def get_area(self):
        return self._bok1 * self._bok2

    def get_diagonal(self):
        return math.sqrt(self._bok1**2 + self._bok2**2)

rec = Rectangle(5,4)
print(rec.bok1)
rec.bok1 = 3
rec.bok1 = 'tekst'
rec.bok1 = [234]
print(rec.bok1)
print(rec.get_diagonal())