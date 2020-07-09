"""
Crie um programa onde o usuário possa digitar cinco
valores númericos e cadastre-os em uma lista, já na posição
correta de inscrição(sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(lista)
