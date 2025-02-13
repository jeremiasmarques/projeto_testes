from datetime import datetime
from classes.Tratamento import Tratamento


class Animal:
    def __init__(self, nome: str, especie: str, idade_estimada: int, sexo: str, raca: str,
                 caracteristicas: str, data_chegada: datetime, data_saida: datetime = None):
        self._nome = nome
        self._especie = especie
        self._idade_estimada = idade_estimada
        self._sexo = sexo
        self._raca = raca
        self._caracteristicas = caracteristicas
        self._data_chegada = data_chegada
        self._data_saida = data_saida
        self._tratamentos = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_especie(self):
        return self._especie

    def set_especie(self, especie):
        self._especie = especie

    def get_idade_estimada(self):
        return self._idade_estimada

    def set_idade_estimada(self, idade_estimada):
        self._idade_estimada = idade_estimada

    def get_sexo(self):
        return self._sexo

    def set_sexo(self, sexo):
        self._sexo = sexo

    def get_raca(self):
        return self._raca

    def set_raca(self, raca):
        self._raca = raca

    def get_caracteristicas(self):
        return self._caracteristicas

    def set_caracteristicas(self, caracteristicas):
        self._caracteristicas = caracteristicas

    def get_data_chegada(self):
        return self._data_chegada

    def set_data_chegada(self, data_chegada):
        self._data_chegada = data_chegada

    def get_data_saida(self):
        return self._data_saida

    def set_data_saida(self, data_saida):
        self._data_saida = data_saida

    def get_tratamentos(self):
        return self._tratamentos

    def adicionar_tratamento(self, tratamento : Tratamento):
        self._tratamentos.append(tratamento)

    def __repr__(self):
        return (f"Animal({self._nome}, {self._especie}, {self._idade_estimada}, {self._sexo}, {self._raca}, "
                f"{self._caracteristicas}, {self._data_chegada}, {self._data_saida}, {self._tratamentos})")
