from classes import Estoque, Pretendente, Voluntario, Doador, Item, Animal, Tratamento, Resgate, Adocao


class BD:
    def __init__(self):
        self.resgates = []
        self.voluntarios = []
        self.pretendentes = []
        self.doadores = []
        self.animais = []
        self.adocoes = []
        self.estoque = 0

        # Adicionando dados iniciais
        self.inicializar_dados()

    def inicializar_dados(self):
        self.pretendentes.append(Pretendente("Pedro", "87987654321", "Rua das Calçadas"))

        self.voluntarios.append(Voluntario("Paulo", "87912345678",
                                           "Rua das Pontes", "Gerente", "8:00~12:00 seg~sex"))

        self.estoque = Estoque("Estoque Central", "Rua dos Animais", self.voluntarios[0])

        self.doadores.append(Doador("Patrick", "patrick@email.com", "Rua das Ruas das Ruas"))

        # Criando itens e adicionando ao estoque
        self.estoque.entrada_item(Item("Fusca", "Veículo", self.doadores[0], 1))
        self.estoque.entrada_item(Item("Saco de ração para vira-latas", "Ração", self.doadores[0], 4))
        self.estoque.entrada_item(Item("Coleira", "Equipamento", self.doadores[0], 8))

        # Criando animal e tratamentos
        self.animais.append(Animal("Sapato", "Cachorro", 3, "Macho",
                                   "Salsicha", "Pelo marrom escuro, sem cauda"))

        self.animais[0].adicionar_tratamento(Tratamento("Tratamento de raiva", "Remédio para raiva",
                                                        "Aplicação do remédio", "2025-02-02 13:00:00"))

        self.animais[0].adicionar_tratamento(Tratamento("Castracao", "Anestesia",
                                                        "Remoção dos testículos", "2025-02-03 07:30:00"))

        # Criando resgate
        self.resgates.append(Resgate("2025-02-01 07:00:00", "Rua dos Rios", [self.animais[0]], [self.voluntarios[0]]))

        # Criando adoção
        self.adocoes.append(Adocao("2025-02-07 09:00:00", "Aprovado", self.animais[0], self.pretendentes[0], "Termo de Adoção"))

    def exibir_menu(self):
        print("\nBem-vindo ao SGRAA - Sistema de Gestão para Adoção de Animais Domésticos\n")

        while True:
            print("\nO que deseja fazer?")
            print("(e) Estoque / (v) Voluntários / (a) Animais / (s) Sair")
            opcao = input("Escolha uma opção: ").strip().lower()

            if opcao == "s":
                print("Saindo do SGRAA... Até logo!")
                break
            elif opcao == "e":
                print("Menu de Estoque ainda não implementado!")  # Futuro: self.menu_estoque()
            elif opcao == "v":
                self.menu_voluntario()
            elif opcao == "a":
                self.menu_animais()
            else:
                print("Opção inválida! Tente novamente.")

    def menu_voluntario(self):
        while True:
            print("\nO que deseja fazer?")
            print("(v) Ver voluntários / (n) Novo Voluntário / (e) Editar voluntário / (s) Sair")
            opcao = input("Escolha uma opção: ").strip().lower()

            if opcao == "s":
                print("Voltando ao menu principal...")
                break
            elif opcao == "v":
                self.ver_voluntarios()
            elif opcao == "n":
                self.novo_voluntario()
            elif opcao == "e":
                self.editar_voluntario()
            else:
                print("Opção inválida! Tente novamente.")

    def ver_pretendentes(self):
        if not self.pretendentes:
            print("Nenhum pretendente cadastrado.")
            return
        print("\nLista de Pretendentes:")
        for i, pretendente in enumerate(self.pretendentes, start=1):
            print(f"{i}. {pretendente.nome} - {pretendente.contato} - {pretendente.endereco}")

    def ver_voluntarios(self):
        if not self.voluntarios:
            print("Nenhum voluntário cadastrado.")
            return
        print("\nLista de Voluntários:")
        for i, voluntario in enumerate(self.voluntarios, start=1):
            print(
                f"{i}. {voluntario.nome} - {voluntario.contato} - {voluntario.endereco} - {voluntario.funcao} - {voluntario.escala}")

    def novo_voluntario(self):
        nome = input("Nome: ").strip()
        contato = input("Contato: ").strip()
        endereco = input("Endereço: ").strip()
        funcao = input("Função: ").strip()
        escala = input("Escala de trabalho: ").strip()

        voluntario = Voluntario(nome, contato, endereco, funcao, escala)
        self.voluntarios.append(voluntario)
        print(f"Voluntário {nome} cadastrado com sucesso!")

    def editar_voluntario(self):
        if not self.voluntarios:
            print("Nenhum voluntário cadastrado para editar.")
            return
        self.ver_voluntarios()
        try:
            index = int(input("Digite o número do voluntário que deseja editar: ")) - 1
            if index < 0 or index >= len(self.voluntarios):
                print("Número inválido.")
                return

            voluntario = self.voluntarios[index]
            print(f"Editando voluntário: {voluntario.nome}")

            voluntario.nome = input(f"Nome ({voluntario.nome}): ").strip() or voluntario.nome
            voluntario.contato = input(f"Contato ({voluntario.contato}): ").strip() or voluntario.contato
            voluntario.endereco = input(f"Endereço ({voluntario.endereco}): ").strip() or voluntario.endereco
            voluntario.funcao = input(f"Função ({voluntario.funcao}): ").strip() or voluntario.funcao
            voluntario.escala = input(f"Horário ({voluntario.escala}): ").strip() or voluntario.escala

            print("Voluntário atualizado com sucesso!")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    def menu_animais(self):
        while True:
            print("\nO que deseja fazer?")
            print(
                "(v) Ver animais / (n) Novo animal / (e) Editar animal / (r) Gerenciar resgates / (a) Gerenciar "
                "adoções / (s) Sair")
            opcao = input("Escolha uma opção: ").strip().lower()

            if opcao == "s":
                print("Voltando ao menu principal...")
                break
            elif opcao == "v":
                self.ver_animais()
            elif opcao == "n":
                self.novo_animal()
            elif opcao == "e":
                self.editar_animal()
            elif opcao == "r":
                self.menu_resgates()
            elif opcao == "a":
                self.menu_adocoes()
            else:
                print("Opção inválida! Tente novamente.")

    def ver_animais(self):
        if not self.animais:
            print("Nenhum animal cadastrado.")
            return
        print("\nLista de Animais:")
        for i, animal in enumerate(self.animais, start=1):
            print(
                f"{i}. {animal.nome} - {animal.especie} - {animal.idade} anos - {animal.sexo} - {animal.raca} - {animal.caracteristicas}")

    def novo_animal(self):
        nome = input("Nome: ").strip()
        especie = input("Espécie: ").strip()
        idade = input("Idade: ").strip()
        sexo = input("Sexo: ").strip()
        raca = input("Raça: ").strip()
        caracteristicas = input("Descrição: ").strip()

        try:
            idade = int(idade)
        except ValueError:
            print("Idade inválida. Usando 0 por padrão.")
            idade = 0

        animal = Animal(nome, especie, idade, sexo, raca, caracteristicas)
        self.animais.append(animal)
        print(f"Animal {nome} cadastrado com sucesso!")

    def editar_animal(self):
        if not self.animais:
            print("Nenhum animal cadastrado para editar.")
            return
        self.ver_animais()
        try:
            index = int(input("Digite o número do animal que deseja editar: ")) - 1
            if index < 0 or index >= len(self.animais):
                print("Número inválido.")
                return

            animal = self.animais[index]
            print(f"Editando animal: {animal.nome}")

            animal.nome = input(f"Nome ({animal.nome}): ").strip() or animal.nome
            animal.especie = input(f"Espécie ({animal.especie}): ").strip() or animal.especie
            idade = input(f"Idade ({animal.idade}): ").strip()
            if idade:
                try:
                    animal.idade = int(idade)
                except ValueError:
                    print("Idade inválida. Mantendo a anterior.")
            animal.sexo = input(f"Gênero ({animal.sexo}): ").strip() or animal.sexo
            animal.raca = input(f"Raça ({animal.raca}): ").strip() or animal.raca
            animal.caracteristicas = input(f"Descrição ({animal.caracteristicas}): ").strip() or animal.caracteristicas

            print("Animal atualizado com sucesso!")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    def ver_resgates(self):
        """Exibe a lista de resgates cadastrados."""
        if not self.resgates:
            print("\nNenhum resgate cadastrado.")
            return

        print("\nLista de Resgates:")
        for idx, resgate in enumerate(self.resgates, start=1):
            print(f"{idx}. {resgate}")  # `__str__` da classe Resgate será chamado automaticamente

    def novo_resgate(self):
        """Cadastra um novo resgate solicitando informações ao usuário."""
        print("\nCadastro de Novo Resgate")

        data = input("Digite a data do resgate (DD/MM/AAAA): ").strip()
        local = input("Digite o local do resgate: ").strip()

        # Selecionar animais já existentes ou adicionar novos
        animais = []
        while True:
            print("\nAnimais cadastrados:")
            self.ver_animais()  # Lista os animais já registrados
            escolha = input("\nEscolha um animal pelo número (ou 'n' para novo, ENTER para finalizar): ").strip()

            if escolha.lower() == 'n':
                self.novo_animal()
                animais.append(self.animais[-1])  # Pega o último animal cadastrado
            elif escolha == '':
                break
            else:
                try:
                    index = int(escolha) - 1
                    if 0 <= index < len(self.animais):
                        animais.append(self.animais[index])
                    else:
                        print("Número inválido!")
                except ValueError:
                    print("Entrada inválida!")

        # Selecionar voluntários já existentes ou adicionar novos
        participantes = []
        while True:
            print("\nVoluntários cadastrados:")
            self.ver_voluntarios()
            escolha = input("\nEscolha um voluntário pelo número (ou 'n' para novo, ENTER para finalizar): ").strip()

            if escolha.lower() == 'n':
                self.novo_voluntario()
                participantes.append(self.voluntarios[-1])  # Pega o último voluntário cadastrado
            elif escolha == '':
                break
            else:
                try:
                    index = int(escolha) - 1
                    if 0 <= index < len(self.voluntarios):
                        participantes.append(self.voluntarios[index])
                    else:
                        print("Número inválido!")
                except ValueError:
                    print("Entrada inválida!")

        # Criar o resgate e adicioná-lo à lista
        novo_resgate = Resgate(data, local, animais, participantes)
        self.resgates.append(novo_resgate)

        print("\nResgate cadastrado com sucesso!")

    def menu_resgates(self):
        while True:
            print("\nO que deseja fazer?")
            print("(v) Ver resgates / (n) Novo resgate / (s) Sair")
            opcao = input("Escolha uma opção: ").strip().lower()

            if opcao == "s":
                print("Voltando ao menu de animais...")
                break
            elif opcao == "v":
                self.ver_resgates()
            elif opcao == "n":
                self.novo_resgate()
            else:
                print("Opção inválida! Tente novamente.")

    def novo_pretendente(self):
        nome = input("Nome: ").strip()
        contato = input("Contato: ").strip()
        endereco = input("Endereço: ").strip()

        pretendente = Pretendente(nome, contato, endereco)
        self.pretendentes.append(pretendente)
        print(f"Pretendente {nome} cadastrado com sucesso!")

    def nova_adocao(self):
        if not self.animais:
            print("Não há animais disponíveis para adoção.")
            return

        if not self.pretendentes:
            print("Não há pretendentes cadastrados.")
            return

        print("\nLista de Animais Disponíveis:")
        animais_disponiveis = [animal for animal in self.animais if not any(
            adocao.animal == animal and adocao.status == "Aprovado" for adocao in self.adocoes)]

        if not animais_disponiveis:
            print("Todos os animais disponíveis já foram adotados.")
            return

        for i, animal in enumerate(animais_disponiveis, start=1):
            print(f"{i}. {animal.nome} - {animal.especie} - {animal.idade} anos")

        try:
            escolha_animal = int(input("Escolha o número do animal: ")) - 1
            if escolha_animal < 0 or escolha_animal >= len(animais_disponiveis):
                raise ValueError
        except ValueError:
            print("Escolha inválida.")
            return

        print("\nLista de Pretendentes:")
        for i, pretendente in enumerate(self.pretendentes, start=1):
            print(f"{i}. {pretendente.nome} - {pretendente.contato}")

        try:
            escolha_pretendente = int(input("Escolha o número do pretendente: ")) - 1
            if escolha_pretendente < 0 or escolha_pretendente >= len(self.pretendentes):
                raise ValueError
        except ValueError:
            print("Escolha inválida.")
            return

        data_adocao = input("Data da adoção (AAAA-MM-DD HH:MM:SS): ").strip()
        status = input("Status da adoção (Pendente/Aprovado/Rejeitado): ").strip()

        if status not in Adocao.STATUS_VALIDOS:
            print("Status inválido. A adoção será marcada como 'Pendente'.")
            status = "Pendente"

        termo = input("Termo de adoção: ").strip()

        animal_escolhido = animais_disponiveis[escolha_animal]
        pretendente_escolhido = self.pretendentes[escolha_pretendente]

        # Criando a adoção e adicionando à lista
        adocao = Adocao(data_adocao, status, animal_escolhido, pretendente_escolhido, termo)
        self.adocoes.append(adocao)
        print(f"Adoção registrada com sucesso para {pretendente_escolhido.nome} e {animal_escolhido.nome}!")

        # Removendo animal da lista de disponíveis, se a adoção foi aprovada
        if status == "Aprovado":
            self.animais.remove(animal_escolhido)

    def ver_adocoes(self):
        """Exibe a lista de adoções registradas."""
        if not self.adocoes:
            print("\nNenhuma adoção cadastrada.")
            return

        print("\nLista de Adoções:")
        for idx, adocao in enumerate(self.adocoes, start=1):
            print(f"{idx}. {adocao}")  # O método __str__ da classe Adocao será chamado

    def menu_adocoes(self):
        while True:
            print("\nO que deseja fazer?")
            print("(v) Ver adoções / (n) Nova adoção / (s) Sair")
            opcao = input("Escolha uma opção: ").strip().lower()

            if opcao == "s":
                print("Voltando ao menu de animais...")
                break
            elif opcao == "v":
                self.ver_adocoes()
            elif opcao == "n":
                self.nova_adocao()
            else:
                print("Opção inválida! Tente novamente.")

