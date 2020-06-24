# Utilizando o Do While em Python
# n = soma = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     soma += n
# print(soma) # o 999 não será incluido na soma.

n = soma = cont = 0
while cont < 10:
    n = int(input('Digite um número: '))
    cont += 1
    if n % 2 != 0:
        continue
    soma += n
print(soma)


