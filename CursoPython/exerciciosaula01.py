#Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas com o valor digitado.

nome = input("Qual é o seu nome? ")
print(nome,"seja bem-vinda(o)")

#Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatda.

dia = input("Digite o seu dia de nascimento: ")
mes = input("Digite mês em que você nasceu: ")
ano = input("Digite o ano em que você nasceu: ")
print("Você nasceu no dia", dia, "de", mes, "de", ano, ". Correto?")

#Crie um script Python que leia dois números e mostre a soma entre eles.

n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")
soma = int(n1) + int(n2)
print("A soma entre", n1, "e", n2, "é igual a", soma)