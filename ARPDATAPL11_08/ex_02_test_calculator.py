import unittest
import ARPDATAPL11_08.ex_00_calculator as calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calculator.Calculator(5, 2)

    def test_sum_normal_values(self):
        assert self.calc.get_sum() == 7

    def test_substract(self):
        assert self.calc.get_substract() == 3

    def test_multiply(self):
        assert self.calc.get_multiply() == 10

    def test_divide(self):
        assert self.calc.get_divide() == 2.5

    def test_divide_zero(self):
        calc = calculator.Calculator(5, 0)
        with self.assertRaises(ZeroDivisionError):
            calc.get_divide()
