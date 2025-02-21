import unittest
import sys
import os
from unittest.mock import patch
from classes import Estoque, Item, Doador, BD

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestEstoque(unittest.TestCase):

    def setUp(self):
        """Cria uma instância do Estoque antes de cada teste"""
        bd = BD()
        self.estoque = Estoque("Estoque", "Local", bd.voluntarios[0])

    # Teste CT12.01: Registro de nova entrada de estoque
    @patch('builtins.input', side_effect=["Ração", "Alimento", "Fulano", "123456789", "Rua X", "100"])
    def test_registro_nova_entrada_estoque(self, mock_input):
        nome_item = "Ração"
        tipo_item = "Alimento"
        doador_nome = "Fulano"
        contato = "123456789"
        endereco = "Rua X"
        quantidade = 100

        doador = Doador(doador_nome, contato, endereco)
        item = Item(nome_item, tipo_item, doador, quantidade)

        # Adiciona o item ao estoque
        self.estoque.entrada_item(item)

        # Verifica se o item foi adicionado corretamente
        self.assertIn(nome_item, self.estoque.itens)
        self.assertEqual(self.estoque.itens[nome_item], quantidade)

    # Teste CT12.02: Saída de item dentro do estoque disponível
    @patch('builtins.input', side_effect=["Ração", "50"])
    def test_saida_item_disponivel(self, mock_input):
        nome_item = "Ração"
        tipo_item = "Alimento"
        doador_nome = "Fulano"
        contato = "123456789"
        endereco = "Rua X"
        quantidade_entrada = 100
        quantidade_saida = 50

        doador = Doador(doador_nome, contato, endereco)
        item = Item(nome_item, tipo_item, doador, quantidade_entrada)
        self.estoque.entrada_item(item)

        # Realiza a saída do item
        self.estoque.saida_item(nome_item, quantidade_saida)

        # Verifica se o estoque foi atualizado corretamente
        self.assertEqual(self.estoque.itens[nome_item], 50)

    # Teste CT12.03: Saída de item sem estoque suficiente
    @patch('builtins.input', side_effect=["Ração", "150"])
    def test_saida_item_sem_estoque_suficiente(self, mock_input):
        nome_item = "Ração"
        tipo_item = "Alimento"
        doador_nome = "Fulano"
        contato = "123456789"
        endereco = "Rua X"
        quantidade_entrada = 100
        quantidade_saida = 150

        doador = Doador(doador_nome, contato, endereco)
        item = Item(nome_item, tipo_item, doador, quantidade_entrada)
        self.estoque.entrada_item(item)

        # Tenta realizar a saída com quantidade maior que o estoque
        with self.assertRaises(ValueError) as context:
            self.estoque.saida_item(nome_item, quantidade_saida)

        # Verifica se o erro foi gerado corretamente
        self.assertEqual(str(context.exception), "Quantidade insuficiente no estoque ou item inexistente.")

    # Teste CT12.04: Entrada de item com quantidade negativa
    @patch('builtins.input', side_effect=["Medicamento", "Medicamento", "Ciclano", "987654321", "Rua Y", "-10"])
    def test_entrada_item_quantidade_negativa(self, mock_input):
        nome_item = "Medicamento"
        tipo_item = "Medicamento"
        doador_nome = "Ciclano"
        contato = "987654321"
        endereco = "Rua Y"
        quantidade_negativa = -10

        doador = Doador(doador_nome, contato, endereco)

        # Tenta adicionar um item com quantidade negativa
        with self.assertRaises(ValueError) as context:
            self.estoque.entrada_item(Item(nome_item, tipo_item, doador, quantidade_negativa))

        # Verifica se o erro foi gerado corretamente
        self.assertEqual(str(context.exception), "A quantidade deve ser maior que zero")


if __name__ == '__main__':
    unittest.main()
