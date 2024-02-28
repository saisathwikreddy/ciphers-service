from django.test import TestCase
from .ciphers import caesar_encode

class CiphersTest (TestCase):
    def test_caesar_encoding_1(self):
        plain_text = 'hello'
        shift = 1
        expected = 'ifmmp'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_caesar_encoding_2(self):
        plain_text = 'winter'
        shift = 3
        expected = 'zlqwhu'
        output = caesar_encode(plain_text, shift)
        self.assertEqual (expected, output)

    def test_caesar_encoding_3(self):
        plain_text = 'zebra'
        shift = 3
        expected = 'cheud'
        output = caesar_encode(plain_text, shift)
        self.assertEqual (expected, output)