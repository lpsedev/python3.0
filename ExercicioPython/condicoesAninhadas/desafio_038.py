'''
DESAFIO 038

Escreva um programa que leia DOIS NUMEROS inteiros e compare-os,
mostrando na tela uma mensagem:

-O PRIMEIRO VALOR é MAIOR
-O SEGUNDO VALOR é MAIOR
-NÃO EXISTE VALOR maior, os dois são IGUAIS.

'''
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
    print('{} é o primeiro e {} é o segundo'.format(num1, num2))
else:
    print('{} é o primeiro e {} é o segundo'.format(num2, num1))