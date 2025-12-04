import os
valores = list()
for i in range(1, 21):
    x = 1
    for j in range(1, 1 + i):
        x *= j
    valores.append([i, x])
print(valores)
nomeDir = os.path.dirname(__file__)
nomeArquivo = f'{nomeDir}fatoriais04.csv'
arqSaida = open(nomeArquivo, 'w')
for lista in valores:
    arqSaida.write(f'{lista[0]};{lista[1]}\n')
arqSaida.close()