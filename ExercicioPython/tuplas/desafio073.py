times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('RANKING NO CAMPEONATO BRASILEIRO:')
for c in range(0, len(times)):
  print(f'{c + 1}º {times[c]}')

print('\nOS 5 PRIMEIROS COLOCADOS: ')
print(times[0:5])

print('\nOS 4 ÚLTIMOS COLOCADOS')
print(times[16:])

ordemAlfabetica = sorted(times)
print('\nLISTA DOS TIMES EM ORDEM ALFABÉTICA')
for c in range(0, len(ordemAlfabetica)):
  print(c + 1, ordemAlfabetica[c])

print('\nEM QUAL POSIÇÃO ESTÁ A CHAPECOENSE?')


posicao = times.index("Chapecoense")
print(f'A chapecoense está na {posicao + 1}º')