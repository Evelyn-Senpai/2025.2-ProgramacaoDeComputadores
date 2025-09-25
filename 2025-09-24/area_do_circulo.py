#01 - Desenvolva um programa em Python que solicite ao usuário o valor do raio de um círculo e, em seguida, calcule e exiba a área do círculo. Utilize a fórmula da área do círculo. Considere o valor de π = 3.1416
raio = int(input("Digite o valor do raio do círculo: "))
area_do_circulo = 3.1416*raio**2
print(f'A área do circulo é = {area_do_circulo:.2f}')