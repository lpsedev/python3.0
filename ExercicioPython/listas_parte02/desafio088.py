"""
Desafio 088

Faça um programa que ajude um jogador da MEGA SENA a criar
palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 a 60 para vcada jogo,
cadastrando tudo em uma lista composta.

"""
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer fazer? '))  # Quantos jogos deseja
totJogo = 1
while totJogo <= quant:  # Delimmita a quantidade de jogos que serão impresso
    cont = 0
    while True:
        num = randint(1, 60)  # randint gera número aleatório de 1 a 60
        if num not in lista:  # caso o número gerado não esteja repetido na lista, ele será incluido.
            lista.append(num)
            cont += 1  # Conta e inclui 6 valores que não estão repetidos.
        if cont >= 6:  # Quando a lista completar 6 valores ele sai do loop.
            break
    lista.sort()
    jogos.append(lista[:])  # Copia a list[lista] e joga dentro da outra lits[jogos].
    lista.clear()  # apaga o valores armazenado na list[lista]
    totJogo += 1  # Contador de jogos do while principal.
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):  # corre a lista jogo e imprime a lista
    print(f'Jogo {i + 1}: {l}')
    sleep(1)  # temporizador
print('==' * 5, '< BOA SORTE! >', '==' * 5)
