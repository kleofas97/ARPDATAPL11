# napisz klase Calculator
# 2 atrybuty ( okreslane przy inicjacji) a i b
# 4 metody do obliczen - (ktore zwracaja wynik odpowiednio mnozenia, dzielenia, dodawania i odejmowania)

# upgrade - 1 - dodaj liczenie ile operacji juz bylo
#     - w danym kalkulatorze
# - we wszystkich kalkulatorach

class Calculator:
    number_of_operation_in_all_cals = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.number_of_operation = 0

    def get_sum(self):
        self.add_counters()
        return self.a + self.b

    def get_substract(self):
        self.add_counters()
        return self.a - self.b

    def get_multiply(self):
        self.add_counters()
        return self.a * self.b

    def def_divide(self):
        self.add_counters()
        return self.a / self.b

    def add_counters(self):
        self.number_of_operation += 1
        Calculator.number_of_operation_in_all_cals += 1


if __name__ == "__main__":
    calc = Calculator(5, 6)
    calc.get_sum()
    calc.get_substract()
    calc.get_multiply()
    calc2 = Calculator(4, 3)
    calc2.get_sum()
    print(f'Liczba operacji w calc1: {calc.number_of_operation}')
    print(f'Liczba operacji w calc2: {calc2.number_of_operation}')
    print(
        f'Liczba operacji we wszystkich kalkulatorach: '
        f'{Calculator.number_of_operation_in_all_cals}')
