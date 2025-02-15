from classes.Pessoa import Pessoa


class Pretendente(Pessoa):
    def __init__(self, nome: str, contato: str, endereco: str):
        super().__init__(nome, contato, endereco)

    def __str__(self):
        return f"Pretendente: {self.nome}, Contato: {self.contato}, Endereço: {self.endereco}"
