print('=-'*20)
print('\033[7;30mAnalisador de Triângulo\033[m')
print('=-'*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimento acima podem formar triângulo')
else:
    print('Os segmentos acima não podem formar triângulo.')