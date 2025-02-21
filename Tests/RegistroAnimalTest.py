import unittest
from datetime import datetime
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.BD import BD

class TestAdocao(unittest.TestCase):

    def setUp(self):
        # Inicializa as variáveis necessárias para os testes
        self.animais = [Animal("Rex", "Cachorro", 3)]
        self.pretendentes = [Pretendente("João", "123456789")]
        self.adocoes = []
        self.sistema = SistemaAdoção(self.animais, self.pretendentes, self.adocoes)

    def test_adocao_bem_sucedida(self):
        with patch('builtins.input', side_effect=["1", "1", "2025-02-20 10:00:00", "Aprovado", "sim"]):
            self.sistema.nova_adocao()
            self.assertEqual(len(self.adocoes), 1)
            self.assertEqual(self.adocoes[0].animal.nome, "Rex")
            self.assertEqual(self.adocoes[0].pretendente.nome, "João")
            self.assertEqual(self.adocoes[0].status, "Aprovado")

    def test_adocao_sem_termo(self):
        with patch('builtins.input', side_effect=["1", "1", "2025-02-20 10:00:00", "Aprovado", ""]):
            with self.assertRaises(ValueError):
                self.sistema.nova_adocao()

    def test_adocao_animal_ja_adotado(self):
        # Simula uma adoção já realizada
        self.sistema.adocoes.append(Adocao("2025-02-19 10:00:00", "Aprovado", self.animais[0], self.pretendentes[0], "sim"))

        with patch('builtins.input', side_effect=["1", "1", "2025-02-20 10:00:00", "Aprovado", "sim"]):
            with self.assertRaises(ValueError):
                self.sistema.nova_adocao()

    def test_adocao_sem_pretendente_cadastrado(self):
        # Remover todos os pretendentes cadastrados
        self.sistema.pretendentes = []

        with patch('builtins.input', side_effect=["1", "1", "2025-02-20 10:00:00", "Aprovado", "sim"]):
            with self.assertRaises(ValueError):
                self.sistema.nova_adocao()

    def test_adocao_escolha_invalida(self):
        with patch('builtins.input', side_effect=["100", "1", "2025-02-20 10:00:00", "Aprovado", "sim"]):
            with self.assertRaises(ValueError):
                self.sistema.nova_adocao()

    def test_status_invalido(self):
        with patch('builtins.input', side_effect=["1", "1", "2025-02-20 10:00:00", "Invalido", "sim"]):
            self.sistema.nova_adocao()
            # Verifica se o status foi corrigido para "Pendente"
            self.assertEqual(self.adocoes[0].status, "Pendente")

if __name__ == '__main__':
    unittest.main()
