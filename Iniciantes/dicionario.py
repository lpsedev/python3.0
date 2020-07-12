"""
Aula de Dicionários
"""
# pessoas = {
#     'Nome': 'Gustavo',
#     'Sexo': 'M',
#     'Idade': 22
# }
#
# print(pessoas)
# print(pessoas['Idade'])
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
# print(pessoas.keys())  # Ele cria um dicionaŕio com a lista de keys.
# print(pessoas.values())  # Ele cria um dicionaŕio com a lista de values.
# print(pessoas.items())  # Cria uma lista composta com tuplas.
#
# pessoas['Nome'] = 'Paulo'
# pessoas['Peso'] = 98.5  # Adicionando CHAVE: VALOR
# #  del pessoas['Idade']  # Exclui a chave declarada
# for k in pessoas.keys():  # Imprime as chaves
#     print(k)
# for v in pessoas.values():  # Imprime os valores
#     print(v)
# for k, v in pessoas.items(): # Imprime chaves: valores
#     print(f' O {k}: {v}')


# Criando uma lista de inserindo dicionários.
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])  # Acessando pelo índice da lista[0] a keys['uf'] do dicionário
print(brasil[1]['sigla'])  # Acessando pelo índice da lista[0] a keys['uf'] do dicionário.

# Como criar dicionário no FOR e adcionar dentro da lista:
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append((estado.copy()))
print(brasil)

# Acessando elementos da lista e as keys e valeus do dicionário.
for e in brasil:
    for k, v in e.items():  # Acessa todos os itens(KEYS:VALUES)
        print(f'{k}: {v}')
    for v in e.values():  # Acesso os valores do dicionário.
        print(v)
    for k in e.keys():  # Acesso todas a keys do dicionário.
        print(k)


