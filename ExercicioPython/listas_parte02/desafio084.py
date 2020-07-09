"""
Faça um programa que leia nome e peso de várias
pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listas com as pessoas mais pesadas.
C) Uma lista com as pessoas mais leves.

"""

pessoas = []
dados = []
contador = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    contador += 1
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N]: ')).lower()[0]
    if 'n' in r:
        break
maior = menor = cont = 0
nome = ''
nome1 = ''
for p in pessoas:
    cont += 1
    if cont == 1:
        nome = p[0]
        maior = p[1]
        nome1 = p[0]
        menor = p[1]
    if p[1] >= maior:
        nome = p[0]
        maior = p[1]
    else:
        maior = maior
        nome = nome

    if p[1] < menor:
        nome1 = p[0]
        menor = p[1]
    else:
        menor = menor
        nome1 = nome1
print('=-=' * 25)
print(f'Foram cadastradas {contador} pessoas')
print(f'O maior peso foi de {nome} com {maior}Kg')
print(f'O menor peso foi de {nome1} com {menor}Kg')