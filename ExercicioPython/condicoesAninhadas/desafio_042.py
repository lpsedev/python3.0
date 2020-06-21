'''
DESAFIO 042:

Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:

-EQUILÁTERO: Todos os lados iguais.
-ISÓSCELES: Dois lados iguais.
-ESCALENO: todos os lados diferentes.

'''

r1 = float(input('Primeiro lado: '))
r2 = float(input('Segundo lado: '))
r3 = float(input('Terceiro lado: '))

if r1 + r2 == r2 + r3 and r2 + r3 == r1 + r3:
    print('ESSE TRIÂNGULO É EQUILÁTERO')
elif r1 + r2 == r2 + r3 and r2 + r3 != r1 + r3:
    print('ESSE TRIÂNGULO É ISÓSCELES')
else:
    print('ESSE TRIÂNGULO É ESCALENO')