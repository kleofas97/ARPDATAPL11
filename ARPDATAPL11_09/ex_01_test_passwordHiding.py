import unittest

import ARPDATAPL11_09.ex_01_passwordHiding as source


class TestHidePassword(unittest.TestCase):

    def test_normal_text(self):
        tekst = "moje_super_tajne_haslo123"
        result = source.hide_password(tekst)
        expected = "mo*e_*up*r_*aj*e_*as*o1*3"
        assert result == expected

    def test_normal_text_2(self):
        tekst = "adam"
        result = source.hide_password(tekst)
        expected = "ad*m"
        assert result == expected

    def test_short_text(self):
        tekst = "ad"
        result = source.hide_password(tekst)
        expected = "ad"
        assert result == expected

    def test_empty_string(self):
        tekst = ""
        result = source.hide_password(tekst)
        expected = ""
        assert result == expected
