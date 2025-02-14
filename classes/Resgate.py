from typing import List

from classes.Animal import Animal
from classes.Voluntario import Voluntario


class Resgate:
    def __init__(self, data: str, local: str, animais: List[Animal], participantes: List[Voluntario]):
        self._data = data
        self._local = local
        self._animais = animais
        self._participantes = participantes

        for i in self._animais:
            i.set_data_chegada(data)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

        for i in self._animais:
            i.set_data_chegada(data)

    def get_local(self):
        return self._local

    def set_local(self, local):
        self._local = local

    def get_animais(self):
        return self._animais

    def set_animais(self, animais):
        self._animais = animais

    def get_participantes(self):
        return self._participantes

    def set_participantes(self, participantes):
        self._participantes = participantes

    def adicionar_animal(self, animal: Animal):
        self._animais.append(animal)

    def adicionar_participante(self, voluntario: Voluntario):
        self._participantes.append(voluntario)

    def __repr__(self):
        return (f"Resgate({self._data}, {self._local}, Animais: {len(self._animais)}, "
                f"Participantes: {len(self._participantes)})")