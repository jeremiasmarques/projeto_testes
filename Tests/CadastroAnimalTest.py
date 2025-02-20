import unittest
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.BD import BD

class TestCadastroAnimais(unittest.TestCase):

    def setUp(self):
        """Cria uma instância do CadastroAnimais antes de cada teste"""
        self.cadastro = BD()

    # Teste 1: Preenchimento correto de todos os campos
    def test_cadastro_animal_sucesso(self):
        # Simula a entrada de dados
        nome = "Bobby"
        especie = "Cachorro"
        idade = 3
        sexo = "M"
        raca = "Labrador"
        caracteristicas = "Pelagem amarela"
        data_chegada = datetime.now().strftime("%d/%m/%Y")
        x =  datetime.now().strftime("%d/%m/%Y")
        animal = self.cadastro.novo_animal_inputs(nome, especie, idade, sexo, raca, caracteristicas, data_chegada)

        self.assertIsNotNone(animal)
        self.assertEqual(animal.nome, nome)
        self.assertEqual(animal.especie, especie)
        self.assertEqual(animal.idade, idade)
        self.assertEqual(animal.sexo, sexo)
        self.assertEqual(animal.raca, raca)
        self.assertEqual(animal.caracteristicas, caracteristicas)

        self.assertEqual(animal.data_chegada, x)

    # Teste 2: Cadastro de animal sem raça definida
    def test_cadastro_animal_sem_raca(self):
        # Simula a entrada de dados sem raça
        nome = "Miau"
        especie = "Gato"
        idade = 2
        sexo = "F"
        raca = ""  # Raça em branco
        caracteristicas = "Pelagem preta"
        data_chegada = "01/02/2023"

        animal = self.cadastro.novo_animal_inputs(nome, especie, idade, sexo, raca, caracteristicas, data_chegada)

        self.assertIsNotNone(animal)
        self.assertEqual(animal.raca, "")

    # Teste 3: Cadastro de animal com data de chegada futura
    def test_cadastro_animal_data_futura(self):
        # Tenta cadastrar com uma data no futuro
        nome = "Rex"
        especie = "Cachorro"
        idade = 1
        sexo = "M"
        raca = "Pitbull"
        caracteristicas = "Pelagem marrom"
        data_chegada = "30/03/2026"  # Data no futuro


        with self.assertRaises(ValueError) as context:
            self.cadastro.novo_animal_inputs(nome, especie, idade, sexo, raca, caracteristicas, data_chegada)

        self.assertEqual(str(context.exception), "Data de cadastro não pode ser no futuro.")

    # Teste 4: Cadastro de animal sem nome
    def test_cadastro_animal_sem_nome(self):
        # Tenta cadastrar com nome vazio
        nome = ""
        especie = "Cachorro"
        idade = 4
        sexo = "M"
        raca = "Golden Retriever"
        caracteristicas = "Pelagem dourada"
        data_chegada = "01/02/2023"

        with self.assertRaises(ValueError) as context:
            self.cadastro.novo_animal_inputs(nome, especie, idade, sexo, raca, caracteristicas, data_chegada)

        self.assertEqual(str(context.exception), "O nome do animal é obrigatório.")

if __name__ == '__main__':
    unittest.main()
