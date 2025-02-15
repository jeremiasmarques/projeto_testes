class Tratamento:
    def __init__(self, descricao: str, medicamentos: str, procedimento: str, datahora: str):
        self._descricao = descricao
        self._medicamentos = medicamentos
        self._procedimento = procedimento
        self._datahora = datahora

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self._descricao = descricao

    @property
    def medicamentos(self):
        return self._medicamentos

    @medicamentos.setter
    def medicamentos(self, medicamentos: str):
        self._medicamentos = medicamentos

    @property
    def procedimento(self):
        return self._procedimento

    @procedimento.setter
    def procedimento(self, procedimento: str):
        self._procedimento = procedimento

    @property
    def datahora(self):
        return self._datahora

    @datahora.setter
    def datahora(self, datahora: str):
        self._datahora = datahora

    def __str__(self):
        return f"Tratamento: {self.descricao}, Medicamentos: {self.medicamentos}, Procedimento: {self.procedimento}, Data/Hora: {self.datahora}"
