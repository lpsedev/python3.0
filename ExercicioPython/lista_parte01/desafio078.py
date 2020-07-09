"""
Desafio 078

Faça um programa que leia 5 valores númericos
e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.
"""
valor = []
print('=-' * 25)
for v in range(0, 5):
    valor.append(int(input(f'Ditige um valor para a posição {v}: ')))
print('=-' * 25)
cont = maior = menor = posicaoMaior = posicaoMenor = 0
for c, v in enumerate(valor):
    cont += 1
    if cont == 1:
        maior = v
        menor = v
    else:
        if maior < v:
            maior = v
            posicaoMaior = c
        else:
            maior = maior
            posicaoMaior = posicaoMaior
        if menor > v:
            menor = v
            posicaoMenor = c
        else:
            menor = menor
            posicaoMenor = posicaoMenor

print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} na {posicaoMaior}ª')
print(f'O maior valor digitado foi {menor} na {posicaoMenor}ª')
print('=-' * 25)