class Pessoa:
    def __init__(self, nome: str, contato: str, endereco: str):
        self._nome = nome
        self._contato = contato
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, contato: str):
        self._contato = contato

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self._endereco = endereco
