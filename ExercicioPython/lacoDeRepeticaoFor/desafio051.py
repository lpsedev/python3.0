'''
DESAFIO 052

Desenvolva um programa que leia o PRIMEIRO TERMO E A RAZÃO de uma PA.
No final, mostre os 10 primeiros termos dessa progressão
'''
ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = ptermo + (10 - 1) * razao
for c in range(ptermo, decimo + 1, razao):
  print(f'{c}', end=' -> ')
print('ACABOU')
