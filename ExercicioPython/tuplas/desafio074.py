"""
Desafio 074
Crie um programa que vai gerar cinco números aleatórios e
colocar em uma tupla.

Depois disso, mostre a lisytagem de números gerados e também indique
o menor e o maior valor que estão na tupla.

"""
from random import randint
resp = ''
cont = maior = menor = 0
numerosAleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in numerosAleatorios:
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        else:
            maior = maior
        if n < menor:
            menor = n
        else:
            menor = menor
print(f'Valores aleatório {numerosAleatorios}')
print(f'O maior valor da tupla é {maior}')
print(f'O menor valor da tupla é {menor}')
