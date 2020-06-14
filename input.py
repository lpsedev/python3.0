# Entrada de Dados

nome = input("Qual o seu nome? ") # Quando ua o input a variável 'nome'
# recebe o que for digitado pelo usuário.
print(f'o usuário digitou {nome}')

# A Função INPUT sempre irá retornar uma string.
number = input("Digite um valor: ")
print(f'O usuario digitou {number} ela é do tipo {type(number)}')

pessoa = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

ano_nascimento = 2020 - int(idade) # Para que ano_nascimento receba um inteiro
# é necessário converter para int.


# Para que uma string se torne um número inteiro é necessário:
# transformá-lo em um nummero inteiro.
num_1 = input("Digite um valor: ")
num_2 = input('Digite outro valor: ')

# A conversão para inteiro
num_1 = int(num_1) # ou assim:
num_1 = int(input("Digite um valor: "))
num_2 = int(num_1) # ou assim:
num_2 = int(input("Digite outro valor: "))



print(f'{nome} tem {idade} anos e é nascido em {ano_nascimento}')

