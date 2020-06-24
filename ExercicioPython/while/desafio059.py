"""
Crie um programa que leia DOIS VALORES e mostre
um MENU na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novas números
[5] sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso.
"""
soma = 0
multiplicacao = 0
maior = 0
novosNumeros = 0
num = 0
while num != 5:
    print('''\t\033[1:35m**** MENÚ DAS OPERAÇÕES ****\033[m
    Escolha uma das opções abaixo:
    \033[1:34m[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA\033[m''')

    n1 = int(input('\tDigite o primeiro valor: '))
    n2 = int(input('\tDigite o segundo valor: '))
    num = int(input('\tDigite a opção escolhida: '))
    if num == 1:
        soma = n1 + n2
        print(f'\t\033[7mA soma dos valores {n1} + {n2} = {soma}\033[m')
    elif num == 2:
        multiplicacao = n1 * n2
        print(f'\t\033[7mA multiplicação dos valores {n1} X {n2} = {multiplicacao}\033[m')
    elif num == 3:
        if n1 > n2:
            print(f'\t\033[7m{n1} é maior que {n2}\033[m')
        else:
            print(f'\t\033[7m{n2} é maior que {n1}\033[m')
    elif num == 4:
        continue
    elif num == 5:
        break
    else:
        print('\t\033[1:41mDigite uma opção válida!\033[m')
        continue
print('\t\033[7:33mFIM\033[m')

