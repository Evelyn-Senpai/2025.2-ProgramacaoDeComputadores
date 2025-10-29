'''
   Imprimir a tabuada de multiplicação de 6
'''
cont = 1
n = int(input('Digite um número: '))
print('Sua tabuada é: ')
while cont != 11:
    print(f'{cont} x {n} = {cont*n}')
    cont += 1