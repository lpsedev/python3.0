# Desafio 066
"""
Crie um programa que leia vários números interios pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram digitadso e qual
foi a soma entre eles.
"""

cont = soma = n = 0
while n != 999:
    n = int(input(('Digite um número: ')))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados um número {cont}X e soma dos valores foi {soma}')