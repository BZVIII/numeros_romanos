import unittest
from romanos import a_numero


class RomanosTests(unittest.TestCase):
    def test_digitos_romanos(self):
        self.assertEqual(a_numero('I'), 1)
        self.assertEqual(a_numero('V'), 5)

    def test_numeros_completos(self):
        self.assertEqual(a_numero('XXV'), 25)
        self.assertEqual(a_numero('CDXXIV'), 424)

    def test_no_se_resta_ni_V_L_D(self):
        with self.assertRaises(ValueError):
            a_numero('VC')
            a_numero('LM')
            a_numero('LD')
            a_numero('DM')


    def test_no_se_resta_mas_de_un_salto(self):
        self.assertEqual(a_numero('IV'), 4)
        self.assertEqual(a_numero('IX'), 9)
        self.assertEqual(a_numero('XL'), 40)
        self.assertEqual(a_numero('XC'), 90)
        self.assertEqual(a_numero('CD'), 400)
        self.assertEqual(a_numero('CM'), 900)
        with self.assertRaises(ValueError):
            a_numero('IL')
            a_numero('IC')
            a_numero('IM')
            a_numero('XM')
            a_numero('XD')

    def tests_no_mas_de_tres_repeticiones(self):
        self.assertEqual(a_numero('III'), 3)
        with self.assertRaises(ValueError):
            a_numero('IIII')

    def test_no_restas_dos_iguales(self):
        with self.assertRaises(ValueError):
            a_numero('CCM')




