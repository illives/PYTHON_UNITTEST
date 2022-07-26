"""
TDD <- Test Driven Development
Ciclo

Fake It Before you make It

Red
Parte 1 <- Criar Teste que falha

Green <- Criar Teste que passe;

Refactor
Parte 3 <- Melhorar o Código.
"""

import unittest
from beacon_tdd import beacon_tdd

class TestBeacon_tdd(unittest.TestCase):
    def test_beacon_tdd_deve_ser_assertion_error_se_nao_for_int(self):
        with self.assertRaises(AssertionError):
            beacon_tdd(" ")
    
    def test_beacon_tdd_deve_retornar_se_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "Sucesso"
        for entrada in entradas:
            with self.subTest(entrada = entrada, saida=saida):
                self.assertEqual(beacon_tdd(entradas, saida))

unittest.main(verbosity=2)