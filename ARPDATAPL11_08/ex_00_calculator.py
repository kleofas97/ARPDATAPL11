# tutorial w temacie getter, setter
# https://www.geeksforgeeks.org/difference-between-attributes-and-properties-in-python/


class Calculator:
    number_of_operation_in_all_cals = 0

    def __init__(self, a, b):
        self._a = a
        self._b = b
        self.number_of_operation = 0

    @property  # getter (zwraca prywatna wartosc, ktora jest do uzytku wewnatrz klasy)
    def a(self):
        return self._a

    @a.setter  #setter
    def a(self, nowe_a):
        # WALIDACJA a
        print(f'Probuje ustawic a na wartosc {nowe_a}')
        if isinstance(nowe_a, (int, float)):
            self._a = nowe_a
        else:
            # liczba nie jest numerem!
            print(f'Nie zmieniono wartosci liczby {self._a}, poniewaz podano wartosc: {nowe_a}')

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, nowe_b):
        # WALIDACJA b
        print(f'Probuje ustawic b na wartosc {nowe_b}')
        if isinstance(nowe_b, (int, float)):
            self._b = nowe_b
        else:
            # liczba nie jest numerem!
            print(f'Nie zmieniono wartosci liczby {self._b}, poniewaz podano wartosc: {nowe_b}')


    def get_sum(self):
        self.add_counters()
        return self._a + self._b

    def get_substract(self):
        self.add_counters()
        return self._a - self._b

    def get_multiply(self):
        self.add_counters()
        return self._a * self._b

    def def_divide(self):
        self.add_counters()
        return self._a / self._b

    def add_counters(self):
        self.number_of_operation += 1
        Calculator.number_of_operation_in_all_cals += 1

if __name__ == "__main__":
    calc = Calculator(5, 6)
    calc.a = 'text'
    print(calc.a)
    print(calc.get_sum())
