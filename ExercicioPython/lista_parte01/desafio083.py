"""
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar
se a expressõa passada está com os parênteses
abertos e fechados na ordem correta.
"""
expresso = str(input('Digite a expressão: '))
pilha = []
for simb in expresso:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')




