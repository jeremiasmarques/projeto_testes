from classes.Pessoa import Pessoa


class Doador(Pessoa):
    def __init__(self, nome: str, contato: str, endereco: str):
        super().__init__(nome, contato, endereco)
        self._historico_doacoes = []

    @property
    def historico_doacoes(self):
        return self._historico_doacoes

    def adicionar_doacao(self, doacao: str):
        self._historico_doacoes.append(doacao)
