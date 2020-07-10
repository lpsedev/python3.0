"""
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final mostre os valoes pares e ímpares em ordem crescente.
"""
# 1ª forma da fazer
# par = []
# impar = []
# lista = []
#
# for n in range(0 ,7):
#     num = int(input('Digite um valor: '))
#     if num % 2 == 0:
#         par.append(num)
#         par.sort()
#     else:
#         impar.append(num)
#         impar.sort()
# lista.append(par[:])
# lista.append(impar[:])
# print(f'Os números pares digitados foram {lista[0]}')
# print(f'Os números ímpares digitados foram {lista[1]}')

# 2ª forma de fazer

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        num[0].append(valor)
        num[0].sort()
    else:
        num[1].append(valor)
        num[1].sort()
print('=-=' * 40)
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')