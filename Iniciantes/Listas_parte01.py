a = [2, 4, 5, 6]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('RESULTADO APÓS O FATIAMENTO')
a = [2, 4, 5, 6]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

