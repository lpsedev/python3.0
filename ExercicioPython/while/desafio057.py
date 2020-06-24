'''
Faça um programa que leia o SEXO de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''
sexo = ''
while sexo != 'M' and sexo != 'F':

    sexo = str(input('Qual o seu sexo? [M/F] '))
    if sexo == 'm' or sexo == 'f':
        print('DIGITE NOVAMENTE!')
print('Obrigado, você digitou a letra correta.')