# Desenvola um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo de um PA: '))
r = int(input('Digite a razão de uma PA: '))

print('Os s 10 primeiros termos dessa progressão são:')
for c in range(1, 11):
    resultado = a1 + (c - 1) * r
    print('a{} = {:.0f} + ({} - 1) x {:.0f} = {}'.format(c,a1,c,r, resultado))