"""
Desafio 070

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. NO final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
resposta = ''
total = maisDeMil = cont = maisBarato = 0
barato = ''
while resposta != 'N':
    produto = str(input('Digite o nome do produto: '))
    preco = int(input('Qual o preço? '))
    cont += 1
    total += preco
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if preco > 1000:
        maisDeMil += 1
    if cont == 1:
        maisBarato = preco
        barato = produto
    else:
        if preco < maisBarato:
            maisBarato = preco
            barato = produto




print('{:-^40}'.format('FIM DE PROGRAMA'))
print(f'O total dos produtos foram R$ {total}')
print(f'A quantidade de produtos acima de R$ 1000,00 foi {cont}')
print(f'Produto de menor preço foi {barato} que custa {maisBarato}')


