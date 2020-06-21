
# TODAS AS INFROMAÇÕES POSSIVÉIS SOBRE UM DADO.
# algo = input('Digite algo: ')
# print(f'{algo} é do tipo {type(algo)}') # tipo
# print(f'{algo} tem espaço? {algo.isspace()}') # Se tem espaço
# print(f'{algo} é um número? {algo.isnumeric()}') # Se é um número.
# print(f'{algo} é alfabético? {algo.isalpha()}') # Se é alfabético
# print(f'{algo} é alfańumérico? {algo.isalnum()}') # Se é alfanumérico
# print(f'{algo} é maiúscula? {algo.isupper()}') # Se é maiúscula
# print(f'{algo} é minúscula? {algo.islower()}') # Se é minúscula
# print(f'{algo} é capitalizada? {algo.istitle()}') # Se é capitalizada.

# ANCECESSOR E SUCESSOR
num = int(input('Digite um número: '))
print(f'Seu antecessor é {num - 1} e seu sucessor é {num + 1}')
# Outra forma de imprimir uma variável.
print('Dada as circunstâncias do valor {}, o seu antecessor é {} e o sucessor é {}'.format(num, (num -1), (num + 1)))