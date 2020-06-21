"""
DESAFIO 036
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa.
O programa vai perguntar, O VALOR DA CASA,
o SALARIO do comprador e em QUANTOS ANOS ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do sálario ou então será negado.

"""
valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Seu salário mensal? '))
qntdAnos = int(input('Em quantos anos deseja pagar? '))

prestacao = int(qntdAnos * (360 / 30))
porMes = float(valorCasa / prestacao)
porcento = salario * 30 / 100

if porMes < porcento:
    print('Empréstimo Aprovado!')
else:
    print('Infelizmente seu empréstimo foi negado.')
print("Agradecemos a preferência!")

