'''
Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o MAIOR eo MENOR peso lidos.
'''
maior = 0
menor = 0
for c in range (0, 6):
    peso = float(input('Qual o seu peso? '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f' MAIOR {maior:.2f} e o MENOR {menor:.2f}')