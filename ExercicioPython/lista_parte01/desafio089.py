"""
Desafio 089

Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.

"""
ficha = []
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if 'N' in resp:
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Nota de qual aluno deseja ver? '))
    if opc > len(ficha) - 1:
        print('Esse aluno não existe, digite novamente.')
        continue
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    print('-' * 35)
    r = str(input('Deseja continuar: [S/N] ')).upper()[0]
    if 'N' in r:
        break
print('-' * 35)
print('FINALIZANDO')



