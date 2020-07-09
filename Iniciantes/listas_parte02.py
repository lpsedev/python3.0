# galera = [['Joao', 19], ['Ana', 33], ['Pedro', 25], ['Luiz', 38], ['Marcos', 21]]
# # print(galera[3][0])
#
# for posicao in galera:
#    # print(posicao)  Imprime as 5 listas de dentro de galera
#    # print(posicao[0]) Imprime somente os nomes de cada lista interna.
#    # print(posicao[1]) imprime somente as idades de cada lista interna.
#     print(f'{posicao[0]} tem {posicao[1]} anos de idade')

pessoas = []
dados = []

for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    pessoas.append(dados[:])
    dados.clear()  # apaga os dados no laço
print(pessoas)

totmai = totmen = 0
for p in pessoas:
    # p[1] averigua se a idade é maior ou menor
    if p[1] >= 21:
        print(f'{p[0]} é ,maior de idade')  # p[0] mostra o nome do maior de idade
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')
