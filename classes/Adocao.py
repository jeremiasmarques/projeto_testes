from datetime import datetime

from classes.Animal import Animal
from classes.Pretedente import Pretendente


class Adocao:
    def __init__(self, data: datetime, status: str, animal: Animal, pretendente: Pretendente, termo_adocao: str):
        self._data = data
        self._status = status
        self._animal = animal
        self._pretendente = pretendente
        self._termo_adocao = termo_adocao

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_animal(self):
        return self._animal

    def set_animal(self, animal : Animal):
        self._animal = animal

    def get_pretendente(self):
        return self._pretendente

    def set_pretendente(self, pretendente : Pretendente):
        self._pretendente = pretendente

    def get_termo_adocao(self):
        return self._termo_adocao

    def set_termo_adocao(self, termo_adocao):
        self._termo_adocao = termo_adocao

    def __repr__(self):
        return (f"Adocao({self._data}, {self._status}, {self._animal}, "
                f"{self._pretendente}, {self._termo_adocao[:30]}...)")
