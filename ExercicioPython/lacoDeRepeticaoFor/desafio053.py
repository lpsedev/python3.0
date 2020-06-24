'''
DESAFIO 053

Crie um programa que leia uma frase qualquer � diga se elqa �
um palidromo, desconsiderando os espa�os.
'''
for c in range(0, 10):
    palavra = str(input('Escreva uma frase: ')).replace(' ', '').upper()
    palavraInvertida = palavra[::-1]
    if palavra == palavraInvertida:
        print(f'A frase {palavra} = {palavraInvertida} É UM POLÍDROMO')
    else:
        print(f'Palavra digitada {palavra} != {palavraInvertida} NÃO É POLÍDROMO')


