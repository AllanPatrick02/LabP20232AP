'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2023/2
Mensagem:  Allan Patrick de Miranda Lima
Anexo:      prova1.py
'''

#1. Faça um programa que leia o valor unitário de um produto,
#   a quantidade desejada e imprima o valor total a pagar. (2,5pt)

def q01():
    
    valor = float(input('Qual o valor do Produto?'))
    quantidade = int(input('Quantos deseja?'))
    total = (valor*quantidade)

    print(f'O valor total é: R${total:.2f}')


#2. Faça um programa que leia 3 números e imprima o maior deles. (2,5pt)
def q02():

    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira outro número: '))
    num3 = int(input('Insira mais um número: '))

    if num1 > num2:
        print(f'{num1} é o maior número!')
    else:
        print(f'{num2} é o maior número!')




#3. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#   reprovação e as demais em prova final). (2,5pt)

def q03():
    nome = input('Insira seu nome: ')
    prova1 = float(input('Insira a nota da Prova 1: '))
    prova2 = float(input('Insira a nota da Prova 2: '))
    media = (prova1+prova2)/2

    print(nome)
    print(f'Sua média foi {media}')
    
    if media <= 3:
        print('REPROVADO!!!')

    if media < 7:
        print('PROVA FINAL!!!')
    
    if media >= 7:
        print('APROVADO!!!')


#4. Faça um programa que apresente um menu com 4 opções:
#   [1] - Cadastrar
#   [2] - Excluir
#   [3] - Pesquisar
#   [0] - Sair
#   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
#   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
#   escolhida for zero (0). (2,5pt)