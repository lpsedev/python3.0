'''
DESAFIO 045:

Crie um programa que faça o computador jogar
JOKENPÔ(PEDRA, PAPEL, TESOURA) com vc:

'''
import random

print('=-'*20)
print('\033[7;30O SEU ADVERSÁRIO SERÁ O COMPUTADOR\033[m')
print('\t\t\033[7;30mJOGO JOKENPÔ\033[m')
print('''
Instruções sobre o Jogo:
- Você irá escolha umas das 3 opçẽos:
* pedra
* papel
* tesoura

 - Caso você escolha a opção certa,
 você será o vencedor.
 ''')
print('=-'*20)

PC = ('pedra', 'papel', 'tesoura')
pc = random.choice(PC)
escolha = str(input('Escolha uma das opções acima: '))

if escolha == 'pedra' and pc == 'tesoura':
    print(f'{escolha} quebra {pc}')
    print('VOCÊ VENCEU!')
elif escolha == 'pedra' and pc == 'papel':
    print(f'{pc} embrulha {escolha}')
    print('COMPUTADOR VENCEU!')
elif escolha == 'tesoura' and pc == 'papel':
    print(f'{escolha} corta {pc}')
    print('VOCÊ VENCEU!')
elif escolha == 'tesoura' and pc == 'pedra':
    print(f'{pc} quebra {escolha}')
    print('COMPUTADOR VENCEU!')
elif escolha == pc:
    print(f'{escolha} EMPATE {pc}')

