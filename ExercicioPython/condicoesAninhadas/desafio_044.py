'''
DESAFIO 044:

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

- A vista DINHEIRO/CHEQUE: 10% de desconto0.
- à vista no CARTÃO: 5% de desconto.
- em até 2X NO CARTÃO: preço normal.
- 3X OU MAIS no cartão: 20% de juros.

'''
pagamento = float(input('Qual o valor a pagar? '))

escolha = int(input('''
Escolha abaixo umas das opções de pagamento:

1 - Pagamento no dinheiro/Cheque -> 10% de desconto
2 - Pagamento à vista no cartão -> 5% de desconto
3 - Pagamento ate 2X no cartão -> sem desconto
4 - Pagamento até 3X no cartão -> 20% de juros
Opção: '''))

dinheiro = float(pagamento * 10 / 100)
cartaoVista = float(pagamento * 5 / 100)
cartao2x = float(pagamento)
cartao3x = float(pagamento * 20 / 100)

if escolha == 1:
    print(f'''Você recebeu 10% de desconto:
     - Valor a pagar -> {pagamento:.2f}
     - Valor com 10% desconto -> {pagamento - dinheiro:.2f}''')
elif escolha == 2:
    print(f'''Você recebeu 5% de desconto:
     - Valor a pagar -> {pagamento:.2f}
     - Valor com 5% desconto -> {pagamento - cartaoVista:.2f}''')
elif escolha == 3:
    print(f'''Obrigado pelo pagamento!
     Valor sem desconto e sem juros -> {cartao2x:.2f}''')
elif escolha == 4:
    print(f'''Será cobrado 20% de juros:
         - Valor a pagar -> {pagamento:.2f}
         - Valor com 20% de juros -> {pagamento + cartao3x:.2f}''')
else:
    print('Digite uma opção válida!')
print('\033[7;30mAGRADECEMOS A PREFERÊNCIA!\033[m')

