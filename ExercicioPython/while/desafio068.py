"""
Desafio 068

Faça um programa que jogue par ou impar com o computador.
O jogo só será interropido quando o jogador perder,
mostrando na tela o total de vitóris consecutivas que ele consquistou
no jogo final.

"""
from random import randint
computador = randint(0, 999)
impar = 1
par = cont = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR:')
while True:
    jogador = int(input('Digite um valor: '))
    escolha = input('PAR OU IMPAR? [P/I] ').upper()
    soma = jogador + computador
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o PC {computador}. O total de {soma} deu PAR')
            print('Você Ganhou!! :)')
            print('Vamos jogar novamente...')
            cont += 1
            print('=-' * 20)
        else:
            print(f'Você jogou {jogador} e o PC {computador}. O total de {soma} deu IMPAR')
            print('Você Perdeu!! :(')
            break

    if escolha == 'I':
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o PC {computador}. O total de {soma} deu IMPAR')
            print('Você Ganhou!! :)')
            print('Vamos jogar novamente...')
            cont += 1
            print('=-' * 20)
        else:
            print(f'Você jogou {jogador} e o PC {computador}. O total de {soma} deu PAR')
            print('Você Perdeu!! :( ')
            break
print('=-' * 20)
print(f'GAME OVER! Você venceu {cont}X')