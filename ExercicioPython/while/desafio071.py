"""
Desafio 071

Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregue.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
saque = 1
while True:
    saque = int(input('Digite o valor a ser sacado: '))
    print(f'Quantidade de cédulas de R$ 50,00 = {int(saque / 50)}')
    saque = saque % 50
    print(f'Quantidade de cédulas de R$ 20,00 = {int(saque / 20)}')
    saque = saque % 20
    print(f'Quantidade de cédulas de R$ 10,00 = {int(saque / 10)}')
    saque = saque % 10
    print(f'Quantidade de cédulas de R$ 1,00 = {int(saque)}')





