'''
DESAFIO 054

Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores.
'''
contMaior = 0
contMenor = 0
for c in range(0, 6):
    nascimento = int(input('Qual o ano do seu nascimento? '))
    idade = 2020 - nascimento
    if idade >= 21:
        contMaior += 1
    else:
        contMenor += 1
print(f'Maiores de idade são {contMaior} '
      f'e os menores de idade são {contMenor}')