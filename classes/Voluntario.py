from classes.Pessoa import Pessoa


class Voluntario(Pessoa):
    def __init__(self, nome: str, contato: str, endereco: str, funcao: str, escala: str):
        super().__init__(nome, contato, endereco)
        self._funcao = funcao
        self._escala = escala

    @property
    def funcao(self):
        return self._funcao

    @funcao.setter
    def funcao(self, funcao: str):
        self._funcao = funcao

    @property
    def escala(self):
        return self._escala

    @escala.setter
    def escala(self, escala: str):
        self._escala = escala

    def __str__(self):
        return f"Voluntário: {self._nome}, Contato: {self._contato}, Função: {self._funcao}, Escala: {self._escala}"

    def __repr__(self):
        return f"Voluntario({self._nome}, {self._contato}, {self._funcao}, {self._escala})"