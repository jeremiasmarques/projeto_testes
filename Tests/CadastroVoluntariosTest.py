import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes import Voluntario, BD

class TestSistemaVoluntarios(unittest.TestCase):
    def setUp(self):
        self.sistema = BD()

    @patch('builtins.input', side_effect=["Ana", "123456789", "Rua das Flores, 123", "Médico", "Diurno"])
    def test_cadastro_sucesso(self, mock_input):
        self.sistema.novo_voluntario()
        self.assertEqual(len(self.sistema.voluntarios), 1)
        voluntario = self.sistema.voluntarios[0]
        self.assertEqual(voluntario.nome, "Ana")
        self.assertEqual(voluntario.contato, "123456789")
        self.assertEqual(voluntario.endereco, "Rua das Flores, 123")
        self.assertEqual(voluntario.funcao, "Médico")
        self.assertEqual(voluntario.escala, "Diurno")

    @patch('builtins.input', side_effect=["Carlos", "987654321", "Av. Central, 45", "", "Noturno"])
    def test_cadastro_funcao_indefinida(self, mock_input):
        self.sistema.novo_voluntario()
        voluntario = self.sistema.voluntarios[0]
        self.assertEqual(voluntario.funcao, "")

    @patch('builtins.input', side_effect=["Bruna", "111222333", "Rua Secundária, 88", "Voluntário", "Somente finais de semana"])
    def test_cadastro_escala_personalizada(self, mock_input):
        self.sistema.novo_voluntario()
        voluntario = self.sistema.voluntarios[0]
        self.assertEqual(voluntario.escala, "Somente finais de semana")

    @patch('builtins.input', side_effect=["Diego", "555666777", "Rua dos &*!@#, 99", "Coordenador", "Integral"])
    def test_cadastro_endereco_caracteres_especiais(self, mock_input):
        self.sistema.novo_voluntario()
        voluntario = self.sistema.voluntarios[0]
        self.assertEqual(voluntario.endereco, "Rua dos &*!@#, 99")

    @patch('builtins.input', side_effect=["", "", "", "", ""])
    def test_cadastro_campos_vazios(self, mock_input):
        with self.assertLogs(level='ERROR') as log:
            self.sistema.novo_voluntario()
        self.assertIn("Erro: Todos os campos são obrigatórios", log.output[0])

    @patch('builtins.input', side_effect=["", "123456789", "Rua X", "Função", "Escala"])
    def test_cadastro_sem_nome(self, mock_input):
        with self.assertLogs(level='ERROR') as log:
            self.sistema.novo_voluntario()
        self.assertIn("Erro: O nome é obrigatório", log.output[0])

    @patch('builtins.input', side_effect=["Ana", "", "Rua X", "Função", "Escala"])
    def test_cadastro_sem_contato(self, mock_input):
        with self.assertLogs(level='ERROR') as log:
            self.sistema.novo_voluntario()
        self.assertIn("Erro: O contato é obrigatório", log.output[0])

    @patch('builtins.input', side_effect=["Ana", "123456789", "Rua X", "Função", ""])
    def test_cadastro_sem_escala(self, mock_input):
        self.sistema.novo_voluntario()
        voluntario = self.sistema.voluntarios[0]
        self.assertTrue(voluntario.escala in ["", "Padrão"])

if __name__ == '__main__':
    unittest.main()
