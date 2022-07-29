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
from unittest.mock import patch
from Pessoal import Pessoa

class TestPessoa(unittest.TestCase):
    
    def setUp(self):
        self.p1 = Pessoa('Luiz', 'Olaviano')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Luiz')

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Olaviano')

    def test_pessoa_attr_nome_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dadosobtidos_tem_o_valor_False(self):
        self.assertFalse(self.p1.dados_obtidos)

    def test_obter_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_dados_Falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)
            
    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)


if __name__=="__main__":
    unittest.main(verbosity=2)