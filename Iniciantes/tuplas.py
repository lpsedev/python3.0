# Em python tupla = (), lista = [] e dicionário = {}.
# Tuplas são imutáveis.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata-fritas')
# for c in lanche:
#     barraca = c

# imprime sem precisar de posição
for c in lanche:
    print(c)

# 1ª) Ele imprime cada item do lanche e a posição de cada item.
for cont in range(0, len(lanche)):
    print(lanche[cont], cont)

# 2ª) Ele imprime cada item do lanche e a posição de cada item.
for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}')

# imprime os itens em sorted(ordem) alfabética
print(sorted(lanche))

# concatena as tuplas | A ORDEM IMPORTA NA TUPLA.
a = (2, 4, 5, 6)
b = (5, 4, 7, 8)
c = b + a
print(c)

# COUNT = contando quantas vezes se repete um valor na tupla.
print(c.count(4))

# INDEX = mostra a posição de um valor
print(c.index(6))

# INDEX = mostra o valor a partir de uma posição:
        #valor, posição
print(c.index(4, 3))

# A tupla aceita qualquer tipo de dados.
pessoa = ('Luiz', 5, 6, 'Maria')




