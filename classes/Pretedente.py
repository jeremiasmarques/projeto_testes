from classes.Pessoa import Pessoa


class Pretendente(Pessoa):
    def __init__(self, nome: str, contato: str, endereco: str):
        super().__init__(nome, contato, endereco)
