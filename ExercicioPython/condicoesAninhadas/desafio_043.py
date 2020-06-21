from math import pow
'''
DESAFIO 043:

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, clacule sua IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade mórbida.

'''
peso =  float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = float(peso / pow(altura, 2))

if imc < 18.5:
    print(f'Você está abaixo do peso -> IMC {imc:.2f}')
elif imc >= 18.5 and imc <= 25:
    print(f'Você está no peso ideal -> IMC {imc:.2f}')
elif imc > 25 and imc <= 30:
    print(f'Você está com sobrepeso -> IMC {imc:.2f}')
elif imc > 30 and imc <= 40:
    print(f'Você está Obeso -> IMC {imc:.2f}')
else:
    print(f'Você está com Obesidade Mórbida -> IMC {imc:.2f}')