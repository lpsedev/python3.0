"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
"""
n = 1
print('=-' * 20)
while n > 0:
    n = int(input('Digite o número da tabuada que deseja: '))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{n} X {c} = {n * c}')
    print('=-' * 20)
print('FIM')
