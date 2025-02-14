from classes import *
from menus import *

pretendente1 = Pretendente("Pedro", "87987654321", "Rua das calcadas")

voluntario1 = Voluntario("Paulo", "87912345678",
                         "Rua das Pontes", "Gerente", "8:00~12:00 seg~sex")

doador1 = Doador("Patrick", "patrick@email.com", "Rua das Ruas das Ruas")

item1 = Item("Fusca", "Veiculo", doador1, 1)
item2 = Item("Saco de racao para viralatas", "Racao", doador1, 4)
item3 = Item("Coleira", "Equipamento", doador1, 8)

animal1 = Animal("Sapato", "cachorro", 3, "Macho",
                 "Salcicha", "Pelo marrom escuro, sem cauda")

tratamento1 = Tratamento("Tratamento de rabica", "Remedio para rabica",
                         "Aplicacao do remedio", "2025-02-02 13:00:00")
tratamento2 = Tratamento("Castracao", "Anestesia",
                         "Remocao dos testiculos", "2025-02-03 07:30:00")

animal1.adicionar_tratamento(tratamento1)
animal1.adicionar_tratamento(tratamento2)

lista = [animal1]
particiantes = [voluntario1]
resgate1 = Resgate("2025-02-01 07:00:00", "Rua dos Rios", lista, particiantes)

adocao1 = Adocao("2025-02-07 09:00:00", "Concluida", animal1, pretendente1, "Termo de Adocao")

estoque1 = Estoque("Estoque Central", "Rua dos Animais", voluntario1)

estoque1.entrada_item(item1)
estoque1.entrada_item(item2)
estoque1.entrada_item(item3)

print("\nBem vindo ao SGRAA- Sistema de Gestão para Adoção de Animais Domésticos\n")
while True:
    print("O que deseja fazer?")
    print("(e) Estoque / (v) Voluntarios / (a) Animais / (s) Sair")

    opcao = str(input()).lower()

    if opcao == "s":
        break

    elif opcao == "e":
        pass

    elif opcao == "v":
        menu_voluntario()

    elif opcao == "a":
        pass

