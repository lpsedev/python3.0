'''
DESAFIO 052
Faça um programa que leia um número inteiro e diga
se ele é ou não primo.
'''

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1:35m', end=' ')
        total += 1
    else:
        print('\033[1:36m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print(f'Por isso {num} é um número primo. ')
else:
    print(f'{num} não é um número primo.')