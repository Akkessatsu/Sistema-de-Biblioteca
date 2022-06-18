# Sistema de Biblioteca - Equipe: João Vítor Maia, Maxwel Gomes, Gabriel Dext, Raul Braga

# Main
from datetime import timedelta, date

# Funções para estilização do console


def Linha():
    print(f'{"":-^73}')

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
                                      #O acervo como o todo. Apenas os livros alugados (que possuem atributo de disponibilidade como false). E os livros como disponíveis (que possuem atributo de disponibildiade como true)
        print(f'{"":-^65}\n'
            f'| {"TÍTULO":^10} | {"AUTOR":^10} | {"DATA DE DEVOLUÇÃO":^10} | {"DISPONIBILIDADE":^10} |\n'
            f'{"":-^65}')
        if escolha == 1:
            for livro in self.livros:
                if livro.disponibilidade == True:
                    livro.status = "Disponível"
                    print(f'| {livro.titulo:^10} | {livro.autor:^10} | {livro.status:^15} |\n'
                    f'{"":-^65}')
                else:
                    livro.status = "Alugado"
                    print(f'| {livro.titulo:^10} | {livro.autor:^10} | {livro.status:^15} |\n')

        elif escolha == 2:
            for livro in self.livros:
                if livro.disponibilidade == True:
                    livro.status = "Disponível"
                    print(f'| {livro.titulo:^10} | {livro.autor:^10} | {livro.status:^15} |\n')

                else:
                    continue
        else:
            for livro in self.livros:
                if livro.disponibilidade == False:
                    livro.status = "Alugado"
                    print(f'| {livro.titulo:^10} | {livro.autor:^10} | {livro.status:^15} |\n')

                else:
                    continue
        print(f'\n')

    def mostrarUsers(self): #Método que visualiza os usuários cadastrados no parâmetro de usuários
        for user in self.users:
            print(f'NOME: {user.nome:<}')
            Linha()

    def multar(self, livro, user, dataAtual): #Método que incrementa o atributo multa do usuário se a data de devolução do seu livro for superior à dataAtual, portanto, estaria atrasado
                                              #Para essa dinâmica de comparação entre datas e definição da data de devolução foram se utilizados os métodos timedelta e date, que realizam e permitem
                                              #usar as classes de datas e suas respectivas operações (comparação, soma, subtração)
            if livro.devolucao > dataAtual:
                deltaT = livro.devolucao - dataAtual
                dias = deltaT.days

                for x in range(0,int(dias)):
                    user.multa += 1

                print(f'O livro em questão está atrasado em {dias} dias!!!\n'
                f'{"":-^73}\n'
                f'(A cada 1 dia de atraso multamos em 1 real...)\n'
                f'{"":-^73}\n'
                f'Sua multa é de: {user.multa}...\n')

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
        print("Empréstimo efetuado com sucesso!!!")

    def devolver(self, livro):      #Método que permite ao usuário do sistema de realizar a devolução de um livro. Isso ocorre em partes poseteriores do código (linha 271 - 281), funcionando de forma
                                    #semelhante ao método de alugar em sua execução com outras partes do código, como explicado acima. O usuário insere o título que deseja devolver e é feito uma procura com
                                    #um loop for, que testa cada parâmetro titulo de cada objeto do array de livros em posse do usuário afim de encontrar o idêntico ao que o usuário inseriu. Quando encontrado
                                    #é realizado a devolução e, com oexplicadop anteriormente, a multa, caso o prazo tenha expirado.
        livro.disponibilidade = True
        livro.devolucao = "---"
        self.livros.remove(livro)
        print("Devolução realizada com sucesso!!!")
        Linha()


# Criando objeto Biblioteca (construtor: [Biblioteca(sem parâmetros)])
biblioteca = Biblioteca()


# Execução do programa
print(f'{" SISTEMA DE BIBLIOTECA ":^148}')

Linha()
print("Por favor, insira a data atual de acordo com o padrão DIA, MÊS E ANO:")
Linha()
dia = int(input("DIA:"))
mes = int(input("MÊS:"))
ano = int(input("ANO:"))
Linha()

# Variáveis de data
dataAtual = date(ano,mes,dia) #Objeto que representa a data atual
diffData = timedelta(days=7) #Representa a diferença entre duas datas, podendo então ser usada para "aumentar" o tempo de datas ou "diminuit" o tempo de datas, sendo esse usado para se definir
                             #a data de devolução, em que é definido por meio da soma da data em que o empréstimo foi realizado em conjunto com o timedelta de diffData

while True:                                         #O funcionamento do código se deu a partir de estruras de decisões, loop's e tratamentos de erro, para o usuário poder realizar diversas operações em apenas um run, e evitar possíveis inputs mal-colocados....
        while True:
            try:
                choice = int(input(
                    f'O que deseja realizar?:\n'
                    f'{"":-^73}\n'
                    f'{"1 - Cadastrar usuário":<}\n'
                    f'{"2 - Cadastrar livro":<}\n'
                    f'{"3 - Listar usuários":<}\n'
                    f'{"4 - Listar livros":<}\n'
                    f'{"5 - Entrar em conta":<}\n'
                    f'{"6 - Sair do sistema":<}\n'
                    f'{"":-^73}\n'))
                Linha()
                if choice <= 0 or choice > 6:
                    print("Digite apenas o solicitado...")
                    Linha()
                    continue
                break
            except(ValueError, TypeError):
                print("Digite apenas o solicitado...")
                Linha()

        if choice == 1:
            nome = input(f'Qual o nome da pessoa a ser cadastrada?:\n'
            f'{"":-^73}\n')
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
            titulo = input(f'Qual o nome do livro a ser cadastrado?:\n'
            f'{"":-^73}\n')
            Linha()
            autor = input(f'Qual o nome do autor do livro?:\n'
            f'{"":-^73}\n')
            Linha()

            if len(biblioteca.livros) == 0:
                biblioteca.cadastrarLivro(titulo,autor)
                continue

            for livro in biblioteca.livros:
                if livro == livro.titulo:
                    Linha()
                    print(f"Livro já cadastrado!"
                    f'{"":-^73}'
                    f"Entre em sua conta...")

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
                                        f'{"":-^73}\n'
                                        f'{"1 - Acervo completo":<}\n'
                                        f'{"2 - Acervo disponível":<}\n'
                                        f'{"3 - Acervo indisponível":<}\n'
                                        f'{"":-^73}\n'))

                    if escolha < 1 or escolha > 3:
                        Linha()
                        print("Digite apenas o solicitado...")
                        continue

                    else:
                        biblioteca.mostrarLivros(escolha)
                        Linha()
                        break

                except(ValueError, TypeError):
                    Linha()
                    print("Digite apenas o solicitado...")
        if choice == 5:
            while True:
                nome = input(f"Qual o usuário?:\n"
                f'{"":-^73}\n')
                Linha()

                for usuario in biblioteca.users:
                    if nome == usuario.nome:
                        while True:
                            try:
                                opcao = int(input(
                                    f"Bem-vindo(a) de volta {nome} !!! "
                                    f'\n{"":-^73}\n'
                                    f"{'Qual operação deseja realizar?:'}\n"
                                    f'{"":-^73}\n'
                                    f"{'1 - Empréstimo'}\n"
                                    f"{'2 - Devolução'}\n"
                                    f"{'3 - Sair da conta'}\n"
                                    f'{"":-^73}\n'))

                                if opcao < 1 or opcao > 3:
                                    Linha()
                                    print("Digite apenas o solicitado...")
                                    continue

                                else:
                                    if opcao == 1:
                                        livro = input(f'{"":-^73}\n'
                                            f'Qual é o livro que deseja alugar?\n'
                                            f'{"":-^73}\n')

                                        for livros in biblioteca.livros:
                                            if livro == livros.titulo:
                                                Linha()
                                                print("Por favor, insira a data do empréstimo de acordo com o padrão DIA, MÊS E ANO:")
                                                Linha()
                                                dia = int(input("DIA:"))
                                                mes = int(input("MÊS:"))
                                                ano = int(input("ANO:"))
                                                Linha()
                                                data = date(ano, mes, dia)

                                                usuario.alugar(livros,data)
                                                Linha()
                                                break
                                        
                                    elif opcao == 2:
                                        livro = input(f'{"":-^73}\n'
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
                        Linha()
                        print("Usuário inserido incorretamente ou não cadastrado...")

                if opcao == 3:
                    Linha()
                    break

        if choice == 6:
            break
