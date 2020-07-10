"""

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valore pares digitados.
B) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.

"""
matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = maior = coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor {l}, {c}: '))
for l in range(0, 3):  # Somando todos os valores par encontrado na matriz
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()  # quebra de linha
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):  # Somando o valores da 3ª coluna
    coluna += matriz[l][2]
print(f'A soma da terceira coluna é {coluna}')
for c in range(0, 3):  # Achando o maior valor da 2ª linha
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é {maior}')