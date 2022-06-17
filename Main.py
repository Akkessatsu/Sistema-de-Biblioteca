# Sistema de Biblioteca - Equipe: João Vítor Maia, Maxwel Gomes, Gabriel Dext, Raul Braga

# Main
from datetime import timedelta, date
from colorama import Back, Fore, Style

# Funções para estilização do console


def Linha():
    print(f'{"":-^30}')

# Classes


class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = True
        self.devolucao = "---"
        self.status = "="


class Biblioteca():
    def __init__(self):
        self.livros = []
        self.users = []

    def cadastrarLivro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))

    def cadastrarPessoa(self, nome):
        self.users.append(user(nome))

    def mostrarLivros(self, escolha):
        print(
            f'{"TÍTULO | AUTOR | Nº EXEMPLAR | DISPONIBILIDADE | DATA DE DEVOLUÇÃO | STATUS"}')
        if escolha == 1:
            for livro in self.livros:
                if livro.disponibilidade == True:
                    livro.status = "Disponível"
                    print(f'{livro.titulo} | {livro.autor} | {livro.devolucao} | {livro.status}')
                else:
                    livro.status = "Alugado"
                    print(f'{livro.titulo} | {livro.autor} | {livro.devolucao} | {livro.status}')

        elif escolha == 2:
            for livro in self.livros:
                if livro.disponibilidade == True:
                    livro.status = "Disponível"
                    print(f'{livro.titulo} | {livro.autor} | {livro.devolucao} | {livro.status}')

                else:
                    continue
        else:
            for livro in self.livros:
                if livro.disponibilidade == False:
                    livro.status = "Alugado"
                    print(f'{livro.titulo} | {livro.autor} | {livro.disponibilidade == False: } | {livro.devolucao} | {livro.status}')

                else:
                    continue
        print(f'{"":-^50}')

    def mostrarUsers(self):
        for user in self.users:
            Linha()
            print(user.nome)

    def multar(self, livro, user, dataAtual):
            if livro.devolucao > dataAtual:
                deltaT = livro.devolucao - dataAtual
                dias = deltaT.days
                print(dias)

                for x in range(0,int(dias)):
                    user.multa += 1

                print(f'O livro em questão está atrasado em {dias} dias!!!'
                f'(A cada 1 dia de atraso multamos em 1 real...)'
                f'Sua multa é de: {user.multa}...')

class user():

    # Atributos
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.multa = 0

    # Métodos
    def alugar(self, livro, data):
        livro.disponibilidade = False
        livro.devolucao = data + diffData
        self.livros.append(livro)
        print("Empréstimo efetuado com sucesso!!!")

    def devolver(self, livro):
        livro.disponibilidade = True
        livro.devolucao = "---"
        self.livros.remove(livro)
        print("Devolução realizada com sucesso!!!")


# Criando objeto Biblioteca (construtor: [Biblioteca(sem parâmetros)])
biblioteca = Biblioteca()


# Execução do programa
print(Fore.CYAN)
print(f'{Fore.RESET + Fore.YELLOW +" SISTEMA DE BIBLIOTECA "+ Fore.RESET + Fore.CYAN:-^148}')
print(Fore.RESET)

print("Por favor, insira a data atual de acordo com o padrão DIA, MÊS E ANO:\n")
dia = int(input("DIA:"))
mes = int(input("MÊS:"))
ano = int(input("ANO:"))

# Variáveis de data
dataAtual = date(ano,mes,dia)
diffData = timedelta(days=7)

while True:
        while True:
            try:
                choice = int(input(
                    f'O que deseja realizar?:\n'
                    f'{"":-^30}\n'
                    f'{"1 - Cadastrar usuário":<}\n'
                    f'{"2 - Cadastrar livro":<}\n'
                    f'{"3 - Listar usuários":<}\n'
                    f'{"4 - Listar livros":<}\n'
                    f'{"5 - Entrar em conta":<}\n'
                    f'{"6 - Sair do sistema":<}\n'
                    f'{"":-^30}\n'))

                if choice <= 0 or choice > 6:
                    Linha()
                    print("Digite apenas o solicitado...")
                    Linha()
                    continue
                break
            except(ValueError, TypeError):
                Linha()
                print("Digite apenas o solicitado...")
                Linha()

        if choice == 1:
            nome = input(f'Qual o nome da pessoa a ser cadastrada?:\n')
            Linha()

            if len(biblioteca.users) == 0:
                biblioteca.cadastrarPessoa(nome)
                continue

            for usuario in biblioteca.users:
                if nome == usuario.nome:
                    print("Usuário já cadastrado!\nEntre em sua conta...")

                else:
                    biblioteca.cadastrarPessoa(nome)
                    break

        if choice == 2:
            titulo = input(f'Qual o nome do livro a ser cadastrado?:\n')
            autor = input(f'Qual o nome do autor do livro?:\n')
            Linha()

            if len(biblioteca.livros) == 0:
                biblioteca.cadastrarLivro(titulo,autor)
                print(biblioteca.livros)
                continue

            for livro in biblioteca.livros:
                if livro == livro.titulo:
                    print("Livro já cadastrado!\nEntre em sua conta...")

                else:
                    biblioteca.cadastrarLivro(titulo,autor)
                    print(biblioteca.livros)
                    break
        if choice == 3:
            biblioteca.mostrarUsers()

        if choice == 4:
            while True:
                try:
                    escolha = int(input(f'O que deseja realizar?:\n'
                                        f'{"":-^30}\n'
                                        f'{"1 - Acervo completo":<}\n'
                                        f'{"2 - Acervo disponível":<}\n'
                                        f'{"3 - Acervo indisponível":<}\n'))
                    Linha()

                    if escolha < 1 or escolha > 3:
                        Linha()
                        print("Digite apenas o solicitado...")
                        continue

                    else:
                        biblioteca.mostrarLivros(escolha)
                        Linha()
                        break

                except(ValueError, TypeError):
                    print("Digite apenas o solicitado...")
        if choice == 5:
            while True:
                nome = input("Qual o usuário?:\n")
                Linha()

                for usuario in biblioteca.users:
                    if nome == usuario.nome:
                        while True:
                            try:
                                opcao = int(input(
                                    f"Bem-vindo(a) de volta {nome} !!! "
                                    f"{'Qual operação deseja realizar?:'}\n"
                                    f"{'1 - Empréstimo de'}\n"
                                    f"{'2 - Devolução'}\n"
                                    f"{'3 - Sair da conta'}\n"))

                                if opcao < 1 or opcao > 3:
                                    print("Digite apenas o solicitado...")
                                    continue

                                else:
                                    if opcao == 1:
                                        livro = input(
                                            f'Qual é o livro que deseja alugar?\n')
                                        Linha()

                                        for livros in biblioteca.livros:
                                            if livro == livros.titulo:
                                                print("Por favor, insira a data do empréstimo de acordo com o padrão DIA, MÊS E ANO:\n")
                                                dia = int(input("DIA:"))
                                                mes = int(input("MÊS:"))
                                                ano = int(input("ANO:"))
                                                data = date(ano, mes, dia)

                                                usuario.alugar(livros,data)
                                                break
                                        
                                    elif opcao == 2:
                                        livro = input(
                                            f'Qual é o livro que deseja devolver?\n')
                                        Linha()

                                        for livros in usuario.livros:
                                            if livro == livros.titulo:
                                                biblioteca.multar(livros, usuario, dataAtual)
                                                usuario.devolver(livros)
                                                break
                                    
                                    else:
                                        break

                            except(TypeError):
                                Linha()
                                print("Digite apenas o solicitado...")

                    else:
                        print("Usuário inserido incorretamente ou não cadastrado...")

                if opcao == 3:
                    break

        if choice == 6:
            break
