"""
Crie um programa que vai ler vários números e colocar
em uma lista.

Depois disso. crie duas listas extras que vão conter
apenas os valores pares e os valores
impares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if resp in 'N':
        break
for p in numeros:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print('=-' * 25)
print(f'Os valores digitados foram {numeros}')
print(f'Os valores pares de lista foram {pares}')
print(f'Os valores impares de lista foram {impares}')
