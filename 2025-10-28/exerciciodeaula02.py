cont = 0
num = 0
par = impar = 0
soma_par = 0
soma_impar = 0
while cont != 10:
    if num % 2 == 0:
        par += 1
        soma_par += soma_par
    else:
        impar += 1
        soma_impar += soma_impar
    cont += 1
    num += 1
    print(cont)
print(f'Entre os 10 números, {par} são pares e a soma é {soma_par} e {impar} são ímpares e a soma é {soma_impar}')