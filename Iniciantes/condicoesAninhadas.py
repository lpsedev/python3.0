nome = str(input("Qual o seu nome? "))
if nome == 'Gustavo':
    print("Que nome bonito!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é bem popular no Brasil.")
elif nome in 'Ana':
    print('Belo nome feminino')
else:
    print("Seu nome é normal!.")
print('Bom dia!')