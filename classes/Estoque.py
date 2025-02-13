from classes.Item import Item
from classes.Voluntario import Voluntario


class Estoque:
    def __init__(self, nome: str, local: str, responsavel: Voluntario):
        self._nome = nome
        self._local = local
        self._responsavel = responsavel
        self._itens = {}
        self._historico_entrada = []
        self._historico_saida = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_local(self):
        return self._local

    def set_local(self, local: str):
        self._local = local

    def get_responsavel(self):
        return self._responsavel

    def set_responsavel(self, responsavel: Voluntario):
        self._responsavel = responsavel

    def get_itens(self):
        return self._itens

    def entrada_item(self, item: Item, quantidade: int):
        if item.get_nome() in self._itens:
            self._itens[item.get_nome()]._quantidade += quantidade
        else:
            self._itens[item.get_nome()] = item
            self._itens[item.get_nome()]._quantidade = quantidade
        self._historico_entrada.append(f"Entrada: {quantidade}x {item.get_nome()}")

    def saida_item(self, item_nome: str, quantidade: int):
        if item_nome in self._itens and self._itens[item_nome]._quantidade >= quantidade:
            self._itens[item_nome]._quantidade -= quantidade
            self._historico_saida.append(f"Saída: {quantidade}x {item_nome}")
            if self._itens[item_nome]._quantidade == 0:
                del self._itens[item_nome]
        else:
            raise ValueError("Quantidade insuficiente no estoque ou item inexistente.")

    def get_historico(self):
        return {
            "Entradas": self._historico_entrada,
            "Saídas": self._historico_saida
        }
