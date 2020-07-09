"""
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final mostre os valoes pares e ímpares em ordem crescente.
"""

numeros = []
par = []
impar = []
for c in range(0, 7):
    numeros.append(int(input('Digite um valor: ')))
for p in numeros:
    if p % 2 == 0:
        par.append(p)
        par.sort()
    else:
        impar.append(p)
        impar.sort()
print('=-=' * 25)
print(f'Esse foram os números pares {par}')
print(f'Esse foram os números impares {impar}')
