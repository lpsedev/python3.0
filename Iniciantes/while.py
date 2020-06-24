n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # Ele não irá contar o 0.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'{par} foi a quantidade valores digitados PAR e {impar} foram os ímpares digitados!')
