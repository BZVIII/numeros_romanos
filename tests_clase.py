import unittest
from romanos import RomanNumber

class RomanNumberClassTests(unittest.TestCase):
    def test_crear_Numero_romano(self):
        uno = RomanNumber(1)
        dos = RomanNumber('II')

        self.assertEqual(uno, 'I')
        self.assertEqual(dos, 'II')

        self.assertEqual(uno.valor, 1)
        self.assertEqual(dos.valor, 2)
        self.assertEqual(uno.cadena, 'I')
        self.assertEqual(dos.cadena, 'II')
