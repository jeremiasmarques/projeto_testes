import unittest
import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes import Tratamento, Animal, BD

import unittest

class TestRegistroTratamento(unittest.TestCase):

    # Cenário 3: Registro de tratamento com sucesso

    def test_registro_tratamento_com_dados_completos(self):
        # Dados de entrada
        animal = "Fido"
        tipo_tratamento = "Vacinação"
        data_inicio = "2025-02-20"
        data_termino = "2025-02-20"
        observacao = "Sem reações adversas"

        # Simular registro de tratamento
        resultado = registrar_tratamento(animal, tipo_tratamento, data_inicio, data_termino, observacao)

        # Verificar se o tratamento foi registrado com sucesso
        self.assertTrue(resultado)
        self.assertEqual(resultado['animal'], animal)
        self.assertEqual(resultado['tipo_tratamento'], tipo_tratamento)
        self.assertEqual(resultado['data_inicio'], data_inicio)
        self.assertEqual(resultado['data_termino'], data_termino)
        self.assertEqual(resultado['observacao'], observacao)

    def test_registro_tratamento_sem_observacao(self):
        # Dados de entrada
        animal = "Fido"
        tipo_tratamento = "Vacinação"
        data_inicio = "2025-02-20"
        data_termino = "2025-02-20"
        observacao = ""

        # Simular registro de tratamento
        resultado = registrar_tratamento(animal, tipo_tratamento, data_inicio, data_termino, observacao)

        # Verificar se o sistema permite o registro sem a observação
        self.assertTrue(resultado)
        self.assertEqual(resultado['animal'], animal)

    def test_registro_tratamento_com_data_de_termino_posterior_a_data_de_inicio(self):
        # Dados de entrada
        animal = "Fido"
        tipo_tratamento = "Vacinação"
        data_inicio = "2025-02-20"
        data_termino = "2025-02-22"
        observacao = "Sem reações adversas"

        # Simular registro de tratamento
        resultado = registrar_tratamento(animal, tipo_tratamento, data_inicio, data_termino, observacao)

        # Verificar se o tratamento foi registrado corretamente
        self.assertTrue(resultado)
        self.assertEqual(resultado['data_inicio'], data_inicio)
        self.assertEqual(resultado['data_termino'], data_termino)

    def test_registro_tratamento_com_codigo_unico_gerado(self):
        # Dados de entrada
        animal = "Fido"
        tipo_tratamento = "Vacinação"
        data_inicio = "2025-02-20"
        data_termino = "2025-02-20"
        observacao = "Sem reações adversas"

        # Simular registro de tratamento
        resultado = registrar_tratamento(animal, tipo_tratamento, data_inicio, data_termino, observacao)

        # Verificar se o código único foi gerado
        self.assertTrue(resultado)
        self.assertTrue("codigo_unico" in resultado)

    # Cenário 4: Tentativa de registro com informações incompletas

    def test_registro_tratamento_sem_nome_do_animal(self):
        # Dados de entrada
        tipo_tratamento = "Vacinação"
        data_inicio = "2025-02-20"
        data_termino = "2025-02-20"
        observacao = "Sem reações adversas"

        # Simular registro de tratamento
        resultado = registrar_tratamento("", tipo_tratamento, data_inicio, data_termino, observacao)

        # Verificar se o sistema exibe erro para falta de nome
        self.assertFalse(resultado)
        self.assertEqual(resultado['erro'], "Nome do animal é obrigatório")

    def test_registro_tratamento_sem_tipo_tratamento(self):
        # Dados de entrada
        animal = "Fido"
        data_inicio = "2025-02-20"
        data_termino = "2025-02-20"
        observacao = "Sem reações adversas"

        # Simular registro de tratamento
        resultado = registrar_tratamento(animal, "", data_inicio, data_termino, observacao)

        # Verificar se o sistema exibe erro para falta de tipo de tratamento
        self.assertFalse(resultado)
        self.assertEqual(resultado['erro'], "Tipo de tratamento é obrigatório")

    def test_registro_tratamento_com_data_de_termino_anterior_a_data_de_inicio(self):
        # Dados de entrada
        animal = "Fido"
        tipo_tratamento = "Vacinação"
        data_inicio = "2025-02-20"
        data_termino = "2025-02-18"
        observacao = "Sem reações adversas"

        # Simular registro de tratamento
        resultado = registrar_tratamento(animal, tipo_tratamento, data_inicio, data_termino, observacao)

        # Verificar se o sistema exibe erro para data de término inválida
        self.assertFalse(resultado)
        self.assertEqual(resultado['erro'], "A data de término não pode ser anterior à data de início")

    def test_registro_tratamento_sem_datas(self):
        # Dados de entrada
        animal = "Fido"
        tipo_tratamento = "Vacinação"
        observacao = "Sem reações adversas"

        # Simular registro de tratamento
        resultado = registrar_tratamento(animal, tipo_tratamento, "", "", observacao)

        # Verificar se o sistema exibe erro para datas ausentes
        self.assertFalse(resultado)
        self.assertEqual(resultado['erro'], "As datas de início e término são obrigatórias")

# Função que simula o processo de registrar o tratamento
def registrar_tratamento(animal, tipo_tratamento, data_inicio, data_termino, observacao):
    # Aqui é onde a lógica de registro do tratamento será implementada.
    # Para fins de teste, a função retorna um dicionário simulando o comportamento esperado.

    if not animal:
        return {'erro': 'Nome do animal é obrigatório'}

    if not tipo_tratamento:
        return {'erro': 'Tipo de tratamento é obrigatório'}

    if not data_inicio or not data_termino:
        return {'erro': 'As datas de início e término são obrigatórias'}

    if data_inicio > data_termino:
        return {'erro': 'A data de término não pode ser anterior à data de início'}

    # Se todas as condições forem atendidas, retorna um "registro" simulado
    return {
        'animal': animal,
        'tipo_tratamento': tipo_tratamento,
        'data_inicio': data_inicio,
        'data_termino': data_termino,
        'observacao': observacao,
        'codigo_unico': 'TRT123456'  # Simulando a geração de um código único
    }

if __name__ == "__main__":
    unittest.main()
