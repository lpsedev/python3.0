'''
DESAFIO 041:

A confederação Nacional de natação precisa de um programa
que leia o ano de nascimento de um atleta
e mostre a sua categoria, de acordo com a idade:

- Até 9 ANOS: MIRIM
- Até 14 ANOS: INFANTIL
- Até 19 ANOS: JUNIOR
- Até 20 ANOS: SÊNIOR
- Acima: MASTER

'''
nascido = int(input('Qual o ano do seu nascimento? '))
idade = 2020 - nascido

if idade <= 9:
    print(f'{idade} anos - categoria MIRIM')
elif idade > 9 and idade <= 14:
    print(f'{idade} anos - categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'{idade} anos - categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print(f'{idade} anos - categoria SÊNIOR')
else:
    print((f'{idade} anos - categoria MASTER'))