listagem = ('Lápis', 1.75,
            'Caderno', 2,
            'Borracha', 2.12,
            'Estojo', 25,
            'transferidor', 4.20,
            'Mochila', 123.88,
            'Canetas', 26.77,
            'Livro', 32.66)
print('-' * 50)
print(f'{"MINHA LISTA DE PREÇOS":^50}')
print('-' * 50)
for item in range(len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<40}', end='')
    else:
        print(f'R$ {listagem[item]:>6.2f}')
print('-' * 50)