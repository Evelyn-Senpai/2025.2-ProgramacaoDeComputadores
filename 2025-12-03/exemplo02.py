valores = list()
for i in range(1, 21):
    x = 1
    for j in range(1, 1 + i):
        x *= j
    valores.append([i, x])
print(valores)
arqSaida = open('fatoriais04.csv', 'a')
for lista in valores:
    arqSaida.write(f'{lista[0]};{lista[1]}\n')
arqSaida.close()