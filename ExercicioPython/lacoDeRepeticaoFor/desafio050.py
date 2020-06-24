'''
DESAFIO 051

Desenvolva um programa que leia 6 n�meros inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitados for impar, desconsidere-o.
'''

soma = 0
cont = 0
for c in range(0, 6):
  n = int(input('Digite um valor: '))
  if n % 2 == 0:
    soma += n
print(f'A soma dos pares é {soma}')