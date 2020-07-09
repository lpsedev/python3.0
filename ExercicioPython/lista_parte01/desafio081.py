"""
Desafio081

Crie um programa que vai ler vários números e colocar uma lista.

Depois disso, mostre:
A) Quantos números foram digitados?
B) A lista de valores ardenada de forma decrescente.
C) Se o valor 5 está ou não na lista.
"""

numeros = []
cont = 0
while True:
    numeros.append(int(input('Digite um valor: ')))
    numeros.sort(reverse=True)
    r = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if r in 'N':
        break
print(f'Foram digitados {len(numeros)} números')
print(f'Os valores digitados na ordem reversa {numeros}')
if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('o número 5 não está na lista')









