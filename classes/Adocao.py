from classes.Animal import Animal
from classes.Pretendente import Pretendente


class Adocao:
    STATUS_VALIDOS = {"Pendente", "Aprovado", "Rejeitado"}

    def __init__(self, data: str, status: str, animal: Animal, pretendente: Pretendente, termo_adocao: str):
        if not isinstance(animal, Animal):
            raise ValueError("O objeto 'animal' deve ser uma instância da classe Animal.")
        if not isinstance(pretendente, Pretendente):
            raise ValueError("O objeto 'pretendente' deve ser uma instância da classe Pretendente.")
        if status not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Use um dos seguintes: {self.STATUS_VALIDOS}")

        self._data = data
        self._status = status
        self._animal = animal
        self._pretendente = pretendente
        self._termo_adocao = termo_adocao
        self._animal.data_saida = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, nova_data: str):
        self._data = nova_data
        self._animal.data_saida(nova_data)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status: str):
        if novo_status not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Use um dos seguintes: {self.STATUS_VALIDOS}")
        self._status = novo_status

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, novo_animal: Animal):
        if not isinstance(novo_animal, Animal):
            raise ValueError("O objeto 'animal' deve ser uma instância da classe Animal.")
        self._animal = novo_animal

    @property
    def pretendente(self):
        return self._pretendente

    @pretendente.setter
    def pretendente(self, novo_pretendente: Pretendente):
        if not isinstance(novo_pretendente, Pretendente):
            raise ValueError("O objeto 'pretendente' deve ser uma instância da classe Pretendente.")
        self._pretendente = novo_pretendente

    @property
    def termo_adocao(self):
        return self._termo_adocao

    @termo_adocao.setter
    def termo_adocao(self, novo_termo: str):
        self._termo_adocao = novo_termo

    def __repr__(self):
        return (f"Adocao(data={self._data}, status={self._status}, animal={self._animal}, "
                f"pretendente={self._pretendente}, termo='{self._termo_adocao[:30]}...')")

    def __str__(self):
        return (f"Adoção realizada em {self._data}\n"
                f"Status: {self._status}\n"
                f"Animal: {self._animal}\n"
                f"Adotante: {self._pretendente}\n"
                f"Termo de Adoção: {self._termo_adocao[:50]}...")
