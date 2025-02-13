class Pessoa:
    def __init__(self, nome: str, contato: str, endereco: str):
        self._nome = nome
        self._contato = contato
        self._endereco = endereco

    def get_nome(self):
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_contato(self):
        return self._contato

    def set_contato(self, contato: str):
        self._contato = contato

    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco: str):
        self._endereco = endereco