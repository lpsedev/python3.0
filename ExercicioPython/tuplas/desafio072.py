"""
Crie um programa qie tenha um tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20)
e mostrá-lo por extenso.
"""

while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    if escolha < 0 or escolha > 20:
        print('DIGITE UM NÚMERO QUE ESTEJA NO INTERVALO DE 0 A 20!')
    else:
        numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                  'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
                  'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
        print(f'VOCÊ DIGITOU O NÚMERO "{numero[escolha].upper()}"')



