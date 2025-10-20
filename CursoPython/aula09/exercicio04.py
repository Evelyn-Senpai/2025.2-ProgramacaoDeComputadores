# Refaça o exercicio06 da aula08, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo de um PA: '))
r = int(input('Digite a razão de uma PA: '))
c = 10

print('Os s 10 primeiros termos dessa progressão são:')
while c > 0:
    resultado = a1 + (c - 1) * r
    print('a{} = {:.0f} + ({} - 1) x {:.0f} = {}'.format(c,a1,c,r, resultado))
    c -= 1