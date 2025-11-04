'''
Crie uma tupla preenchida com os 10 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense.
'''
times = ('Palmeiras', 'Flamengo', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Vasco Gama', 'Corinthians', 'Gremio')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os primeiros 5 colocados são: {times[0:5]}')
print(f'Os últimos 4 colocados são: {times[6:10]}')
print(f'Lista em ordem alfabética: {sorted(times)}')