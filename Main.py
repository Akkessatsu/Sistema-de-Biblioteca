# Sistema de Biblioteca - Equipe: João Vítor Maia, Maxwel Gomes, Gabriel Dext, Raul Braga

# Main
from datetime import timedelta, date
from time import sleep

# Funções para estilização do console
import colorama; from colorama import Fore, Back, Style, init;
init()

def Linha():
    print(f'{Fore.RESET}'
        f'{Fore.CYAN}'
        f'{"":-^73}'
        f'{Fore.RESET}')

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  #Código para limpar o console
        command = 'cls'
    os.system(command)


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

    def cadastrarLivro(self, titulo, autor): #FMétodo que cadastra os livros criando dinamicamente objetos e adicionando-os ao atributo livros.
        self.livros.append(Livro(titulo, autor))

    def cadastrarPessoa(self, nome): #Método que cadastra os usuários criando dinamicamente objetos e adicionando-os ao atributo users.
        self.users.append(user(nome))

    def mostrarLivros(self, escolha): #Método que visualiza o acervo de livros cadastrados (objetos de livros presentes no parâmetro users) permitindo filtra de 3 formas:
        print(Fore.RESET)                              #O acervo como o todo. Apenas os livros alugados (que possuem atributo de disponibilidade como false). E os livros como disponíveis (que possuem atributo de disponibildiade como true)
        print(f'{Fore.CYAN}'
            f'{"":-^45}\n'
            f'{Fore.RESET}'
            f'{Fore.CYAN}|{Fore.RESET} {Fore.RED}{"TÍTULO":^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.RED}{"AUTOR":^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.RED}{"DISPONIBILIDADE":^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET}\n'
            f'{Fore.CYAN}'
            f'{"":-^45}'
            f'{Fore.RESET}')
        if escolha == 1:
            for livro in self.livros:
                if livro.disponibilidade == True:
                    livro.status = "Disponível"
                    print(f'{Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.titulo:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.autor:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.status:^15}{Fore.RESET} {Fore.CYAN}|{Fore.RESET}\n'
                    f'{Fore.CYAN}'
                    f'{"":-^45}'
                    f'{Fore.RESET}')
                else:
                    livro.status = "Alugado"
                    print(f'{Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.titulo:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.autor:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.status:^15}{Fore.RESET} {Fore.CYAN}|{Fore.RESET}\n'
                    f'{Fore.CYAN}'
                    f'{"":-^45}'
                    f'{Fore.RESET}')

        elif escolha == 2:
            for livro in self.livros:
                if livro.disponibilidade == True:
                    livro.status = "Disponível"
                    print(f'{Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.titulo:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.autor:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.status:^15}{Fore.RESET} {Fore.CYAN}|{Fore.RESET}\n'
                    f'{Fore.CYAN}'
                    f'{"":-^45}'
                    f'{Fore.RESET}')
        else:
            for livro in self.livros:
                if livro.disponibilidade == False:
                    livro.status = "Alugado"
                    print(f'{Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.titulo:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.autor:^10}{Fore.RESET} {Fore.CYAN}|{Fore.RESET} {Fore.YELLOW}{livro.status:^15}{Fore.RESET} {Fore.CYAN}|{Fore.RESET}\n'
                    f'{Fore.CYAN}'
                    f'{"":-^45}'
                    f'{Fore.RESET}')
                else:
                    continue
        print(f'\n')

    def mostrarUsers(self): #Método que visualiza os usuários cadastrados no parâmetro de usuários
        for user in self.users:
            print(f'{Fore.MAGENTA}NOME:{Fore.RESET}' 
            f"{Fore.YELLOW}{user.nome:<}{Fore.YELLOW}")
            sleep(2)
            Linha()

    def multar(self, livro, user, dataAtual): #Método que incrementa o atributo multa do usuário se a data de devolução do seu livro for superior à dataAtual, portanto, estaria atrasado
                                              #Para essa dinâmica de comparação entre datas e definição da data de devolução foram se utilizados os métodos timedelta e date, que realizam e permitem
                                              #usar as classes de datas e suas respectivas operações (comparação, soma, subtração)
            if livro.devolucao < dataAtual:
                deltaT = livro.devolucao - dataAtual
                dias = deltaT.days

                for x in range(0,int(dias)):
                    user.multa += 1

                print(f'{Fore.RED}O livro em questão está atrasado em{Fore.RESET} {Fore.YELLOW}{dias}{Fore.RESET} {Fore.RED}dias!!!{Fore.RESET}\n'
                f'{Fore.CYAN}'
                f'{"":-^73}\n'
                f'{Fore.RESET}'
                f'{Fore.LIGHTGREEN_EX}'
                f'(A cada 1 dia de atraso multamos em 1 real...)\n'
                f'{Fore.RESET}'
                f'{Fore.CYAN}'
                f'{"":-^73}\n'
                f'{Fore.RESET}'
                f'{Fore.RED}Sua multa é de:{Fore.RESET} {Fore.YELLOW}{user.multa}{Fore.RESET}{Fore.RED} R$...{Fore.RESET}\n')

class user():

    # Atributos
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.multa = 0

    # Métodos
    def alugar(self, livro, data):  #Método que permite ao usuário do sistema de realizar o empréstimo de um livro. Isso é feito em partes posteriores do código (linha 250 - linha 267)
                                    #em que, ao usuário selecionar o título que deseja, tal é procurado por meio de um loop for que compara o atributo titulo dos objetos com o inserido pelo usuário
                                    #,isso com o intuito de se achar o livro em que ele deseja. Achando o objeto com atributo igual ao requisitado, o livro é adicionado à lista de livros do usuário e
                                    #perde sua disponbiilidade (se torna alugado).
        livro.disponibilidade = False
        livro.devolucao = data + diffData
        self.livros.append(livro)
        print(f"{Fore.RED}Empréstimo efetuado com sucesso!!!\n"
        f'A data de entrega foi definida para:{Fore.RESET} {Fore.YELLOW}{livro.devolucao.strftime("%d/%m/%Y")}{Fore.RESET}')

    def devolver(self, livro):      #Método que permite ao usuário do sistema de realizar a devolução de um livro. Isso ocorre em partes poseteriores do código (linha 271 - 281), funcionando de forma
                                    #semelhante ao método de alugar em sua execução com outras partes do código, como explicado acima. O usuário insere o título que deseja devolver e é feito uma procura com
                                    #um loop for, que testa cada parâmetro titulo de cada objeto do array de livros em posse do usuário afim de encontrar o idêntico ao que o usuário inseriu. Quando encontrado
                                    #é realizado a devolução e, com oexplicadop anteriormente, a multa, caso o prazo tenha expirado.
        livro.disponibilidade = True
        livro.devolucao = "---"
        self.livros.remove(livro)
        print(f"{Fore.RED}Devolução realizada com sucesso!!!{Fore.RESET}")
        Linha()


# Criando objeto Biblioteca (construtor: [Biblioteca(sem parâmetros)])
biblioteca = Biblioteca()


# Execução do programa
print(f'{Fore.CYAN}'
    f'{Fore.RESET + Fore.RED + " SISTEMA DE BIBLIOTECA " + Fore.RESET + Fore.CYAN :-^148}\n'
    f'{Fore.RESET}')

Linha()
print(f'{Fore.RED}'
    f"Por favor, insira a data atual de acordo com o padrão DIA, MÊS E ANO:"
    f'{Fore.RESET}')
Linha()
dia = int(input(f'{Fore.MAGENTA}'
    f"DIA:"
    f'{Fore.RESET}'
    f'{Fore.YELLOW}'))
mes = int(input(f'{Fore.RESET}'
    f'{Fore.MAGENTA}'
    f"MÊS:"
    f'{Fore.RESET}'
    f'{Fore.YELLOW}'))
ano = int(input(f'{Fore.RESET}'
    f'{Fore.MAGENTA}'
    f"ANO:"
    f'{Fore.RESET}'
    f'{Fore.YELLOW}'))
Linha()
clearConsole()

# Variáveis de data
dataAtual = date(ano,mes,dia) #Objeto que representa a data atual
diffData = timedelta(days=7) #Representa a diferença entre duas datas, podendo então ser usada para "aumentar" o tempo de datas ou "diminuit" o tempo de datas, sendo esse usado para se definir
                             #a data de devolução, em que é definido por meio da soma da data em que o empréstimo foi realizado em conjunto com o timedelta de diffData

while True:                                         #O funcionamento do código se deu a partir de estruras de decisões, loop's e tratamentos de erro, para o usuário poder realizar diversas operações em apenas um run, e evitar possíveis inputs mal-colocados....
        while True:
            try:
                clearConsole()
                choice = int(input(f'{Fore.RED}'
                    f'O que deseja realizar?:\n'
                    f'{Fore.RESET}'
                    f'{Fore.CYAN}'
                    f'{"":-^73}\n'
                    f'{Fore.RESET}'
                    f'{Fore.MAGENTA}'
                    f'{"1 - Cadastrar usuário":<}\n'
                    f'{"2 - Cadastrar livro":<}\n'
                    f'{"3 - Listar usuários":<}\n'
                    f'{"4 - Listar livros":<}\n'
                    f'{"5 - Entrar em conta":<}\n'
                    f'{"6 - Sair do sistema":<}\n'
                    f'{Fore.RESET}'
                    f'{Fore.CYAN}'
                    f'{"":-^73}\n'
                    f'{Fore.RESET}'
                    f'{Fore.YELLOW}'))
                Linha()
                if choice <= 0 or choice > 6:
                    print(f'{Fore.LIGHTGREEN_EX}'
                        f"Digite apenas o solicitado...")
                    Linha()
                    sleep(2)
                    continue
                break
            except(ValueError, TypeError):
                Linha()
                print(f'{Fore.LIGHTGREEN_EX}'
                    f"Digite apenas o solicitado...")
                Linha()
                sleep(2)

        if choice == 1:
            clearConsole()
            nome = input(f'{Fore.MAGENTA}'
                f'Qual o nome da pessoa a ser cadastrada?:\n'
                f'{Fore.RESET}'
                f'{Fore.CYAN}'
                f'{"":-^73}\n'
                f'{Fore.RESET}'
                f'{Fore.YELLOW}')
            Linha()

            if len(biblioteca.users) == 0:
                biblioteca.cadastrarPessoa(nome)
                continue

            for usuario in biblioteca.users:
                if nome == usuario.nome:
                    print(f'{Fore.LIGHTGREEN_EX}'
                        f"Usuário já cadastrado!"
                        f"\nEntre em sua conta..."
                        f'{Fore.RESET}')
                    sleep(2)

                else:
                    biblioteca.cadastrarPessoa(nome)
                    break

        if choice == 2:
            clearConsole()
            titulo = input(f'{Fore.MAGENTA}'
                f'Qual o nome do livro a ser cadastrado?:\n'
                f'{Fore.RESET}'
                f'{Fore.CYAN}'
                f'{"":-^73}\n'
                f'{Fore.RESET}'
                f'{Fore.YELLOW}')
            Linha()
            clearConsole()
            autor = input(f'{Fore.MAGENTA}'
                f'Qual o nome do autor do livro?:\n'
                f'{Fore.RESET}'
                f'{Fore.CYAN}'
                f'{"":-^73}\n'
                f'{Fore.RESET}'
                f'{Fore.YELLOW}')
            Linha()

            if len(biblioteca.livros) == 0:
                biblioteca.cadastrarLivro(titulo,autor)
                continue

            for livro in biblioteca.livros:
                if livro == str(livro.titulo):
                    Linha()
                    print(f'{Fore.LIGHTGREEN_EX}'
                        f"Livro já cadastrado!"
                        f'{Fore.RESET}'
                        f'{Fore.CYAN}'
                        f'{"":-^73}'
                        f'{Fore.RESET}'
                        f'{Fore.LIGHTGREEN_EX}'
                        f"Entre em sua conta..."
                        f'{Fore.RESET}')
                    sleep(2)
                else:
                    biblioteca.cadastrarLivro(titulo,autor)
                    break
        if choice == 3:
            biblioteca.mostrarUsers()
            sleep(5)
        if choice == 4:
            while True:
                try:
                    clearConsole()
                    escolha = int(input(f'{Fore.RED}'
                                        f'O que deseja realizar?:\n'
                                        f'{Fore.RESET}'
                                        f'{Fore.CYAN}'
                                        f'{"":-^73}\n'
                                        f'{Fore.RESET}'
                                        f'{Fore.MAGENTA}'
                                        f'{"1 - Acervo completo":<}\n'
                                        f'{"2 - Acervo disponível":<}\n'
                                        f'{"3 - Acervo indisponível":<}\n'
                                        f'{Fore.RESET}'
                                        f'{Fore.CYAN}'
                                        f'{"":-^73}\n'
                                        f'{Fore.RESET}'
                                        f'{Fore.YELLOW}'))

                    if escolha < 1 or escolha > 3:
                        Linha()
                        print(f"{Fore.LIGHTGREEN_EX}Digite apenas o solicitado...{Fore.RESET}")
                        sleep(2)
                        continue

                    else:
                        biblioteca.mostrarLivros(escolha)
                        Linha()
                        sleep(5)
                        break

                except(ValueError, TypeError):
                    Linha()
                    print(f"{Fore.LIGHTGREEN_EX}Digite apenas o solicitado...{Fore.RESET}")
                    sleep(2)
        if choice == 5:
            while True:
                clearConsole()
                nome = input(f"{Fore.MAGENTA}Qual o usuário?:{Fore.RESET}\n"
                f'{Fore.CYAN}{"":-^73}{Fore.RESET}\n'
                f'{Fore.YELLOW}')
                Linha()

                for usuario in biblioteca.users:
                    if nome == str(usuario.nome):
                        while True:
                            try:
                                clearConsole()
                                opcao = int(input(
                                    f"{Fore.RED}Bem-vindo(a) de volta{Fore.RESET} {Fore.YELLOW}{nome}{Fore.RESET} {Fore.RED}!!!{Fore.RESET} "
                                    f'{Fore.CYAN}'
                                    f'\n{"":-^73}\n'
                                    f'{Fore.RESET}'
                                    f'{Fore.MAGENTA}'
                                    f"{'Qual operação deseja realizar?:'}\n"
                                    f'{Fore.RESET}'
                                    f'{Fore.CYAN}'
                                    f'{"":-^73}\n'
                                    f'{Fore.RESET}'
                                    f'{Fore.MAGENTA}'
                                    f"{'1 - Empréstimo'}\n"
                                    f"{'2 - Devolução'}\n"
                                    f"{'3 - Sair da conta'}\n"
                                    f'{Fore.RESET}'
                                    f'{Fore.CYAN}'
                                    f'{"":-^73}\n'
                                    f'{Fore.RESET}'
                                    f'{Fore.YELLOW}'))

                                if opcao < 1 or opcao > 3:
                                    Linha()
                                    print(f"{Fore.LIGHTGREEN_EX}Digite apenas o solicitado...{Fore.RESET}")
                                    sleep(2)
                                    continue

                                else:
                                    if opcao == 1:
                                        clearConsole()
                                        livro = input(f'{Fore.RESET}'
                                            f'{Fore.CYAN}'
                                            f'{"":-^73}\n'
                                            f'{Fore.RESET}'
                                            f'{Fore.MAGENTA}'
                                            f'Qual é o livro que deseja alugar?\n'
                                            f'{Fore.RESET}'
                                            f'{Fore.CYAN}'
                                            f'{"":-^73}\n'
                                            f'{Fore.RESET}'
                                            f'{Fore.YELLOW}')

                                        for livros in biblioteca.livros:
                                            if livro == str(livros.titulo):
                                                Linha()
                                                print(f"{Fore.RED}Por favor, insira a data do empréstimo de acordo com o padrão DIA, MÊS E ANO:{Fore.RESET}")
                                                Linha()
                                                dia = int(input(f'{Fore.MAGENTA}'
                                                    f"DIA:"
                                                    f'{Fore.RESET}'
                                                    f'{Fore.YELLOW}'))
                                                mes = int(input(f'{Fore.RESET}'
                                                    f'{Fore.MAGENTA}'
                                                    f"MÊS:"
                                                    f'{Fore.RESET}'
                                                    f'{Fore.YELLOW}'))
                                                ano = int(input(f'{Fore.RESET}'
                                                    f'{Fore.MAGENTA}'
                                                    f"ANO:"
                                                    f'{Fore.RESET}'
                                                    f'{Fore.YELLOW}'))
                                                Linha()
                                                data = date(ano, mes, dia)
                                                usuario.alugar(livros,data)
                                                Linha()
                                                break
                                        
                                    elif opcao == 2:
                                        clearConsole()
                                        livro = input(f'{Fore.CYAN}'
                                            f'{"":-^73}\n'
                                            f'{Fore.RESET}'
                                            f'{Fore.RED}Qual é o livro que deseja devolver?{Fore.RESET}{Fore.YELLOW}\n')
                                        Linha()

                                        for livros in usuario.livros:
                                            if livro == str(livros.titulo):
                                                biblioteca.multar(livros, usuario, dataAtual)
                                                usuario.devolver(livros)
                                                sleep(2)
                                                break
                                    
                                    else:
                                        break

                            except(TypeError,ValueError):
                                Linha()
                                print(f"{Fore.LIGHTGREEN_EX}Digite apenas o solicitado...{Fore.RESET}")
                                sleep(2)

                    else:
                        Linha()
                        print(f"{Fore.LIGHTGREEN_EX}Usuário inserido incorretamente ou não cadastrado...{Fore.RESET}")
                        sleep(2)    

                if opcao == 3:
                    Linha()
                    break

        if choice == 6:
            break
