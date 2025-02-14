class Tratamento:
    def __init__(self, descricao : str, medicamentos : str, procedimento : str, datahora : str):
        self.descricao = descricao
        self.medicamentos = medicamentos
        self.procedimentos = procedimento
        self.datahora = datahora

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_medicamentos(self):
        return self.medicamentos

    def set_medicamentos(self, medicamentos):
        self.medicamentos = medicamentos

    def get_procedimentos(self):
        return self.procedimentos

    def set_procedimentos(self, procedimentos):
        self.procedimentos = procedimentos

    def get_data(self):
        return self.data

    def set_data(self, datahora):
        self.datahora = datahora