"""
Melhore o jogo do DESAFIO 028 onde o computador
vai 'pensar' em um número entre 0 e 10. Só que
agora o jogador vai tentar advinhar até acertar,
mostrando no final quantos palpites foram
necessários para vencer.
"""
from random import randint
tentativas = 0
numSecreto = randint(1, 10)
jogador = 0
while jogador != numSecreto:
    jogador = int(input('Tente advinhar o número secreto: '))
    if jogador == numSecreto:
        break
    else:
        print('Errou!!! Continue tentando')
        tentativas += 1
print(f'PARABÉNS VOCÊ ACERTOU O NÚMERO SECRETO É {numSecreto}')
print(f'O número de tentativas foram {tentativas}')