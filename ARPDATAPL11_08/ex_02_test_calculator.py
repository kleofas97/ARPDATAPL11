import unittest
import ARPDATAPL11_08.ex_00_calculator as calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calculator.Calculator(5,2)

    def test_sum_normal_values(self):
        assert self.calc.get_sum() == 7

    def test_substract(self):
        assert self.calc.get_substract() == 3