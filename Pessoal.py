import requests

class Pessoa:
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def nome_completo(self, nome, sobrenome):
        assert isinstance(nome, str)
        assert isinstance(sobrenome, str)

    def obter_todos_os_dados(self):
        response = requests.get('https://liveuamap.com/')

        if response.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'