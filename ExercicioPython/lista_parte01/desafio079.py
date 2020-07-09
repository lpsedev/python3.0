"""
Desafio 079

Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso!')
    else:
        print('Valor ja existente!')
    r = str(input('Deseja continuar [S/N]: '))
    if r in 'Nn':
        break
lista.sort()
print(lista)