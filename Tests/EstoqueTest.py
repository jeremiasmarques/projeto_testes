import unittest
import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes import Estoque, Item, Doador, BD

class TestSistemaEstoque(unittest.TestCase):
    def setUp(self):
        self.sistema = BD()

    def test_registro_nova_entrada(self):
        self.sistema.adicionar_item("Arroz", 10, "2025-02-20")
        self.assertEqual(self.sistema.estoque["Arroz"].quantidade, 10)

    def test_saida_item_dentro_estoque(self):
        self.sistema.adicionar_item("Feijão", 5, "2025-02-20")
        self.sistema.retirar_item("Feijão", 3)
        self.assertEqual(self.sistema.estoque["Feijão"].quantidade, 2)

    def test_entrada_item_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            self.sistema.adicionar_item("Macarrão", -5, "2025-02-20")

    def test_retirada_item_sem_estoque_suficiente(self):
        self.sistema.adicionar_item("Leite", 2, "2025-02-20")
        with self.assertRaises(ValueError):
            self.sistema.retirar_item("Leite", 5)

    def test_retirada_item_inexistente(self):
        with self.assertRaises(KeyError):
            self.sistema.retirar_item("Óleo", 1)

    def test_retirada_quantidade_negativa(self):
        self.sistema.adicionar_item("Sal", 10, "2025-02-20")
        with self.assertRaises(ValueError):
            self.sistema.retirar_item("Sal", -3)

    def test_retirada_parcial_estoque_insuficiente(self):
        self.sistema.adicionar_item("Açúcar", 3, "2025-02-20")
        with self.assertRaises(ValueError):
            self.sistema.retirar_item("Açúcar", 5)

    def test_bloqueio_retirada_validade_expirada(self):
        self.sistema.adicionar_item("Leite em pó", 5, "2023-01-01")  # Data expirada
        with self.assertRaises(ValueError):
            self.sistema.retirar_item("Leite em pó", 2)

if __name__ == '__main__':
    unittest.main()
