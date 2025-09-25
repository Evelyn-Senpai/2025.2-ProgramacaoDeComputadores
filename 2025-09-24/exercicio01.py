#01 - Desenvolva um programa em Python que solicite ao usuário o valor do raio de um círculo e, em seguida, calcule e exiba a área do círculo. Utilize a fórmula da área do círculo. Considere o valor de π = 3.1416
raio = int(input("Digite o valor do raio do círculo: "))
area_do_circulo = 3.1416*raio**2
print(f'A área do circulo é = {area_do_circulo:.2f}')

#02 - Desenvolva um programa em Python que solicite ao usuário os valores da base maior, base menor e altura de um trapézio e, em seguida, calcule e exiba a sua área. Utilize a fórmula da área do trapézio.
baseMA = float(input('Digite o valor da área maior: '))
baseME = float(input('Digite o valor da área menor: '))
alt = float(input('Digite o valor da altura: '))
area_do_trapezio = (baseMA+baseME)*alt/2
print(f'A área do trapézio é: {area_do_trapezio}')

#03Desenvolva um programa em Python que solicite ao usuário dois valores e em seguida calcule a média aritmética entre eles.
v1 = int(input('Digite o primeiro valor valor: '))
v2 = int(input('Digite o segundo valor valor: '))
media = (v1+v2)/2
print(f'A média é = {media}')