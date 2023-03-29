from unittest import TestCase
from ARPDATAPL11_08.ex_01_Rectangle_get_set import Rectangle
import numpy as np


class TestRectangle(TestCase):

    def setUp(self) -> None:
        self.rec = Rectangle(5, 5)

    def test_bok1(self):
        expected = 10
        self.rec.bok1 = expected
        assert self.rec.bok1 == expected
        not_expected = 'tekst'
        self.rec.bok1 = not_expected
        assert self.rec.bok1 != not_expected

    def test_bok2(self):
        expected = 10
        self.rec.bok1 = expected
        assert self.rec.bok1 == expected
        not_expected = 'tekst'
        self.rec.bok2 = not_expected
        assert self.rec.bok2 != not_expected

    def test_get_area(self):
        self.rec.bok1 = 10
        self.rec.bok2 = 10
        assert self.rec.get_area() == 100

    def test_get_diagonal(self):
        self.rec.bok1 = 3
        self.rec.bok2 = 4
        assert self.rec.get_diagonal() == 5.0

    def test_get_diagonal_wymierna(self):
        self.rec.bok1 = 10
        self.rec.bok2 = 10
        wynik = np.round(self.rec.get_diagonal(), 2)
        assert wynik == np.round(np.sqrt(200), 2)

    def test_negative_numbers_bok1(self):
        not_expected = -10
        self.rec.bok1 = not_expected
        assert self.rec.bok1 != not_expected

    def test_negative_numbers_bok2(self):
        not_expected = -10
        self.rec.bok2 = not_expected
        assert self.rec.bok2 != not_expected
