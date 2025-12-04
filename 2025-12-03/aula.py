valores = list()
for i in range(1, 21):
    x = 1
    for j in range(1, 1 + i):
        x *= j
    valores.append([i, x])
print(valores)
arqSaida = open('fatoriais.txt', 'w')
arqSaida.write(str(valores))
arqSaida.close()