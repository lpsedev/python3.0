palavras = ('aprender', 'programar', 'linguegem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'futuro', 'trabalhar', 'mercado', 'programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(),end='')