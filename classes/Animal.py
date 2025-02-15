from classes.Tratamento import Tratamento


class Animal:
    def __init__(self, nome: str, especie: str, idade: int, sexo: str, raca: str,
                 caracteristicas: str, data_chegada: str = "", data_saida: str = ""):
        self._nome = nome
        self._especie = especie
        self._idade = idade
        self._sexo = sexo
        self._raca = raca
        self._caracteristicas = caracteristicas
        self._data_chegada = data_chegada
        self._data_saida = data_saida
        self._tratamentos = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, especie: str):
        self._especie = especie

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo: str):
        self._sexo = sexo

    @property
    def raca(self):
        return self._raca

    @raca.setter
    def raca(self, raca: str):
        self._raca = raca

    @property
    def caracteristicas(self):
        return self._caracteristicas

    @caracteristicas.setter
    def caracteristicas(self, caracteristicas: str):
        self._caracteristicas = caracteristicas

    @property
    def data_chegada(self):
        return self._data_chegada

    @data_chegada.setter
    def data_chegada(self, data_chegada: str):
        self._data_chegada = data_chegada

    @property
    def data_saida(self):
        return self._data_saida

    @data_saida.setter
    def data_saida(self, data_saida: str):
        self._data_saida = data_saida

    @property
    def tratamentos(self):
        return self._tratamentos

    def adicionar_tratamento(self, tratamento: Tratamento):
        self._tratamentos.append(tratamento)

    def __str__(self):
        return (f"Animal: {self.nome}, Espécie: {self.especie}, Idade: {self.idade}, Sexo: {self.sexo}, "
                f"Raça: {self.raca}, Características: {self.caracteristicas}, "
                f"Data Chegada: {self.data_chegada}, Data Saída: {self.data_saida}")

    def __repr__(self):
        return (f"Animal({self.nome}, {self.especie}, {self.idade}, {self.sexo}, {self.raca}, "
                f"{self.caracteristicas}, {self.data_chegada}, {self.data_saida}, {self.tratamentos})")
