"""
DESAFIO 039

Faça um programa que leia o ano de nascimento de um jovem e informa,
de acordo com a sua idade:
-Se ele AINDA VAI SE ALISTAR ao serviço militar.
-Se é a HORA DE SE ALISTAR.
-Se já PASSOU DO TEMPO do alistamento.
Seu programa também deverá mostrar o tempo que falta ou
que passou o prazo.
"""
nascido = int(input('Digite o ano do seu nascimento: '))
idade = 2020 - nascido
if idade == 18:
    print(f'{idade} anos é a idade para se alistar.')
elif idade < 18:
    falta = 18 - idade
    print(f'{idade} anos ainda falta {falta} anos para se alistar.')
else:
    atrasado = idade - 18
    print(f'{idade} anos você já passou do prazo a {atrasado} anos')


