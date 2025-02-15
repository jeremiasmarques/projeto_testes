from typing import List
from classes.Animal import Animal
from classes.Voluntario import Voluntario


class Resgate:
    def __init__(self, data: str, local: str, animais: List[Animal], participantes: List[Voluntario]):
        self._data = data
        self._local = local
        self._animais = list(animais)  # Cópia para evitar modificação externa
        self._participantes = list(participantes)  # Cópia para evitar modificação externa

        # Define a data de chegada para todos os animais resgatados
        for animal in self._animais:
            if isinstance(animal, Animal):
                animal.data_chegada = data
            else:
                raise ValueError("Todos os itens da lista 'animais' devem ser instâncias de Animal")

        for voluntario in self._participantes:
            if not isinstance(voluntario, Voluntario):
                raise ValueError("Todos os itens da lista 'participantes' devem ser instâncias de Voluntario")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, nova_data: str):
        self._data = nova_data
        for animal in self._animais:
            animal.data_chegada(nova_data)

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, novo_local: str):
        self._local = novo_local

    @property
    def animais(self):
        return self._animais[:]  # Retorna uma cópia para evitar modificações externas

    def adicionar_animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self._animais.append(animal)
            animal.data_chegada(self._data)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância de Animal")

    @property
    def participantes(self):
        return self._participantes[:]

    def adicionar_participante(self, voluntario: Voluntario):
        if isinstance(voluntario, Voluntario):
            self._participantes.append(voluntario)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância de Voluntario")

    def __repr__(self):
        return (f"Resgate(data={self._data}, local={self._local}, "
                f"Animais={len(self._animais)}, Participantes={len(self._participantes)})")

    def __str__(self):
        animais_str = ", ".join([str(animal) for animal in self._animais])
        participantes_str = ", ".join([str(part) for part in self._participantes])
        return (f"Resgate em {self._local} na data {self._data}\n"
                f"Animais resgatados: {animais_str}\n"
                f"Participantes: {participantes_str}")
