import ARPDATAPL11_07.ex_02_calculator as calculator

calc = calculator.Calculator(5, 6)
calc.get_sum()
calc.get_substract()
calc.get_multiply()
calc2 = calculator.Calculator(4, 3)
calc2.get_sum()
print(f'Liczba operacji w calc1: {calc.number_of_operation}')
print(f'Liczba operacji w calc2: {calc2.number_of_operation}')
print(
    f'Liczba operacji we wszystkich kalkulatorach: '
    f'{calculator.Calculator.number_of_operation_in_all_cals}')
