#02 - Desenvolva um programa em Python que solicite ao usuário os valores da base maior, base menor e altura de um trapézio e, em seguida, calcule e exiba a sua área. Utilize a fórmula da área do trapézio.
baseMA = float(input('Digite o valor da área maior: '))
baseME = float(input('Digite o valor da área menor: '))
alt = float(input('Digite o valor da altura: '))
area_do_trapezio = (baseMA+baseME)*alt/2
print(f'A área do trapézio é: {area_do_trapezio}')