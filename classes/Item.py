from classes.Doador import Doador


class Item:
    def __init__(self, nome: str, tipo: str, doador: Doador, quantidade: int):
        if not isinstance(doador, Doador):
            raise ValueError("O doador deve ser uma instância da classe Doador")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")

        self._nome = nome
        self._tipo = tipo
        self._doador = doador
        self._quantidade = quantidade

        # Adiciona o item ao histórico de doações do doador
        self._doador.adicionar_doacao(f"{self._quantidade}x {self._nome} ({self._tipo})")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self._tipo = tipo

    @property
    def doador(self):
        return self._doador

    @doador.setter
    def doador(self, doador: Doador):
        if not isinstance(doador, Doador):
            raise ValueError("O doador deve ser uma instância da classe Doador")
        self._doador = doador  # Removendo a adição automática ao histórico

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        self._quantidade = quantidade

    def __str__(self):
        return f"Item: {self._nome}, Tipo: {self._tipo}, Quantidade: {self._quantidade}, Doador: {self._doador.nome}"
