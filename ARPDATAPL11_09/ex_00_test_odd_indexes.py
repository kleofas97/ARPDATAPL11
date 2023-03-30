import unittest
import ARPDATAPL11_09.ex_00_odd_indexes as source


class TestOddIndexes(unittest.TestCase):

    def test_odd_indexes_normal_text(self):
        assert source.odd_indexes('Teleturniej'), 'eeune'

    def test_odd_indexes_normal_text_2(self):
        self.assertEqual(source.odd_indexes('Tekst'), 'es')

    def test_odd_indexes_one_letter(self):
        self.assertEqual(source.odd_indexes('T'), '')

    def test_odd_indexes_number(self):
        self.assertEqual(source.odd_indexes(5), None)

    def test_odd_indexes_list(self):
        self.assertEqual(source.odd_indexes([1, 2, 3]), None)
