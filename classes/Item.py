from classes.Doador import Doador


class Item:
    def __init__(self, nome: str, tipo: str, doador: Doador, quantidade: int):
        self._nome = nome
        self._tipo = tipo
        self._doador = doador
        self._quantidade = quantidade

        # Adiciona o item ao histórico de doações do doador
        self._doador.adicionar_doacao(f"{self._quantidade}x {self._nome} ({self._tipo})")

    def get_nome(self):
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo: str):
        self._tipo = tipo

    def get_doador(self):
        return self._doador

    def set_doador(self, doador: Doador):
        self._doador = doador
        self._doador.adicionar_doacao(f"{self._quantidade}x {self._nome} ({self._tipo})")

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade: int):
        self._quantidade = quantidade