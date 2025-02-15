from classes.Item import Item
from classes.Voluntario import Voluntario
from typing import Dict, List


class Estoque:
    def __init__(self, nome: str, local: str, responsavel: Voluntario):
        self._nome = nome
        self._local = local
        self._responsavel = responsavel
        self._itens: Dict[str, int] = {}  # Agora armazena apenas nome e quantidade
        self._historico_entrada: List[Dict] = []
        self._historico_saida: List[Dict] = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, local: str):
        self._local = local

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, responsavel: Voluntario):
        self._responsavel = responsavel

    @property
    def itens(self):
        return self._itens.copy()  # Retorna uma cópia para evitar modificações externas

    def entrada_item(self, item: Item):
        """Adiciona um item ao estoque, somando quantidades se já existir."""
        nome = item.nome
        quantidade = item.quantidade

        if quantidade <= 0:
            raise ValueError("A quantidade de entrada deve ser maior que zero.")

        self._itens[nome] = self._itens.get(nome, 0) + quantidade
        self._historico_entrada.append({"tipo": "Entrada", "item": nome, "quantidade": quantidade})

    def saida_item(self, item_nome: str, quantidade: int):
        """Remove uma quantidade específica de um item do estoque."""
        if quantidade <= 0:
            raise ValueError("A quantidade de saída deve ser maior que zero.")

        if item_nome in self._itens and self._itens[item_nome] >= quantidade:
            self._itens[item_nome] -= quantidade
            self._historico_saida.append({"tipo": "Saída", "item": item_nome, "quantidade": quantidade})

            if self._itens[item_nome] == 0:
                del self._itens[item_nome]  # Remove item do estoque se a quantidade chegar a zero
        else:
            raise ValueError("Quantidade insuficiente no estoque ou item inexistente.")

    @property
    def historico(self):
        """Retorna o histórico de entradas e saídas do estoque."""
        return {
            "Entradas": self._historico_entrada,
            "Saídas": self._historico_saida
        }

    def __repr__(self):
        return f"Estoque(nome={self._nome}, local={self._local}, itens={len(self._itens)})"

    def __str__(self):
        itens_str = ", ".join([f"{nome}: {qtd}" for nome, qtd in self._itens.items()])
        return (f"Estoque {self._nome} localizado em {self._local}\n"
                f"Responsável: {self._responsavel}\n"
                f"Itens armazenados: {itens_str if itens_str else 'Nenhum'}")
