'''
DESAFIO 037

Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a BASE DE CONVERSÃO:

-1 PARA BINÁRIO
-2 PARA OCTAL
-3 PARA HEXADECIMAL
'''
numero = int(input('Digite um número: '))

opcao = int(input("""
Qual base binária deseja converter:
1 - BINÁRIO:
2 - OCTAL
3 - HEXADECIMAL

Digite a opção escolhida: """))

if opcao == 1:
    print('BINÁRIO: ',bin(numero))
elif opcao == 2:
    print('OCTADECIMAL: ',oct(numero))
else:
    print('HEXADECIMAL: ',hex(numero))



