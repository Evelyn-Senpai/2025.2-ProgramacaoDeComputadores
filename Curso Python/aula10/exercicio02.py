'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
mult = 1
cont = 1
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if valor <= 0:
        break
    for c in range(1, 11):
        mult = valor * cont
        print(f'{valor} x {cont} = {mult}')
        cont += 1
    print('-'*40)
    cont = 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')