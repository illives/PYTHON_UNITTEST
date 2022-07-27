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
    
    def test_beacon_tdd_deve_retornar_sucesso_se_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Sucesso'

        for entrada in entradas:
            with self.subTest(entrada = entrada, saida=saida):
                self.assertEqual(beacon_tdd(entrada), saida)

    def test_beacon_tdd_deve_retornar_Falha_se_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7)
        saida = 'Falha'

        for entrada in entradas:
            with self.subTest(entrada = entrada, saida=saida):
                self.assertEqual(beacon_tdd(entrada), saida)

    def test_beacon_tdd_deve_retornar_Sucesso_se_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Sucesso'

        for entrada in entradas:
            with self.subTest(entrada = entrada, saida=saida):
                self.assertEqual(beacon_tdd(entrada), saida, msg=f'{entrada} não retornou saida {saida}')

    def test_beacon_tdd_deve_retornar_Sucesso_se_for_multiplo_de_5(self):
        entradas = (5, 10 , 20, 25)
        saida = 'Sucesso'

        for entrada in entradas:
            with self.subTest(entrada = entrada, saida=saida):
                self.assertEqual(beacon_tdd(entrada), saida, msg=f'{entrada} não retornou saida {saida}')

unittest.main(verbosity=2)