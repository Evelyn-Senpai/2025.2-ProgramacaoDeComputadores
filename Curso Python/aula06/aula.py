# STYLE
# 0 = None
# 1 = Bold
# 4 = Underline
# 7 = Negative

# TEXT
# 30 = Branco
# 31 = Vermelho
# 32 = Verde
# 33 = Amarelo
# 34 = Azul
# 35 = Roxo
# 36 = Ciano
# 37 = Cinza

# BACK
# 40 = Branco
# 41 = Vermelho
# 42 = Verde
# 43 = Amarelo
# 44 = Azul
# 45 = Roxo
# 46 = Ciano
# 47 = Cinza

print('\033[0;30;41mTeste')
mundo = 'Mundo'
cores = {'Limpa':'\033[m',
         'Vermelho':'\033[7;41m'}
print('Olá {}{}{}!!!!'.format(cores['Vermelho'], mundo, cores['Limpa']))