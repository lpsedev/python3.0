"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o 9
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
par = 0
print('=' * 40)
num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))
for c in num:
    if c % 2 == 0:
        par = c
print(f'Você digitou os valores {num}')
print('=' * 40)
print(f'O número 9 apareceu {num.count(9)}X')
print('=' * 40)
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)}ª posição')
else:
    print('O valor 3 não foi encontrado entre os números digitados.')
print('=' * 40)
print(f'O número par digitado foi {par}')



