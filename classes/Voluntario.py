from classes.Pessoa import Pessoa


class Voluntario(Pessoa):
    def __init__(self, nome: str, contato: str, endereco: str, funcao: str, escala: str):
        super().__init__(nome, contato, endereco)
        self._funcao = funcao
        self._escala = escala

    def get_funcao(self):
        return self._funcao

    def set_funcao(self, funcao: str):
        self._funcao = funcao

    def get_escala(self):
        return self._escala

    def set_escala(self, escala: str):
        self._escala = escala