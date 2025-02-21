import os
import sys
import unittest
from datetime import datetime

from classes import Animal, Pretendente, Adocao, BD

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestAdocao(unittest.TestCase):

    def setUp(self):
        # Inicializa as variáveis necessárias para os testes
        self.animais = [Animal("Rex", "Cachorro", 3, "Macho",
                               "Salsicha", "Pelo marrom escuro, sem cauda")]
        self.pretendentes = [Pretendente("João", "123456789", "Rua Inexistente")]
        self.adocoes = []
        self.sistema = BD()

    def test_adocao_bem_sucedida(self):
        self.adocoes.append(
            Adocao(datetime.now().strftime("%d/%m/%Y"), "Aprovado", self.animais[0], self.pretendentes[0], "Termo"))
        self.assertEqual(len(self.adocoes), 1)
        self.assertEqual(self.adocoes[0].animal.nome, "Rex")
        self.assertEqual(self.adocoes[0].pretendente.nome, "João")
        self.assertEqual(self.adocoes[0].status, "Aprovado")

    def test_adocao_sem_termo(self):
        with self.assertRaises(ValueError):
            self.sistema.nova_adocao_inputs(None, None, None, None, None)

    def test_adocao_animal_ja_adotado(self):
        # Simula uma adoção já realizada
        self.sistema.adocoes.append(
            Adocao("2025-02-19 10:00:00", "Aprovado", self.animais[0], self.pretendentes[0], "sim"))

        with self.assertRaises(ValueError):
            self.sistema.nova_adocao_inputs("2025-02-19 10:00:00", "Aprovado", self.animais[0], self.pretendentes[0],
                                            "sim")

    def test_adocao_sem_pretendente_cadastrado(self):
        # Remover todos os pretendentes cadastrados
        self.sistema.pretendentes = []

        with self.assertRaises(ValueError):
            self.sistema.nova_adocao_inputs("2025-02-19 10:00:00", "Aprovado", self.animais[0], self.pretendentes[0],
                                            "sim")

    def test_adocao_pretendente_invalida(self):
        with self.assertRaises(ValueError):
            self.sistema.nova_adocao_inputs("2025-02-19 10:00:00", "Aprovado", self.animais[0], None, "Sim")

    def test_status_invalido(self):
        self.sistema.nova_adocao_inputs("2025-02-19 10:00:00", "Aprovado", self.animais[0], self.pretendentes[0], "sim")
        # Verifica se o status foi corrigido para "Pendente"
        self.assertEqual(self.sistema.adocoes[-1].status, "Aprovado")


if __name__ == '__main__':
    unittest.main()
