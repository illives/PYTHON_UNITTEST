try:
    import sys, os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../Script'
            )
        )
    )
except:
    raise

import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(Calculadora.soma(15, 30), 45)

    def test_soma_menos5_e_mais5_deve_retornar_0(self):
        self.assertEqual(Calculadora.soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (2, 3, 5),
            (-5, 5, 0),
            (105, 45, 150)
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida= x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(Calculadora.soma(x,y), saida)
    
    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Calculadora.soma('11', 30)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Calculadora.soma(30, '13')

    def test_subtrair_x_menos_y_retorna_0(self):
        self.assertEqual(Calculadora.subtrair(10, 10), 0)

    def test_subtrair_x_menos_y_retorna_menos_5(self):
        self.assertEqual(Calculadora.subtrair(-5, 0), -5)

    def test_subrair_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Calculadora.subtrair('11', 30)

    def test_subtrair_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Calculadora.subtrair(30, '13')

if __name__ == "__main__":
    unittest.main(verbosity=2)

