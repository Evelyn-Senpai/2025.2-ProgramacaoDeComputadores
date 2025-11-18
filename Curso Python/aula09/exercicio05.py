# Melhore o exercicio04, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

a1 = int(input('Digite o primeiro termo de um PA: '))
r = int(input('Digite a razão de uma PA: '))
c = 10
mais = 1
cont = 0

print('Os 10 primeiros termos dessa progressão são:')

while mais != 0:
    while c > 0:
        resultado = a1 + (c - 1) * r
        print('a{} = {:.0f} + ({} - 1) x {:.0f} = {}'.format(c,a1,c,r, resultado))
        c -= 1
        cont +=1
    mais = int(input('Quantos termos você quer mostrar mais? '))
    cont += mais
    c = cont
print(cont)