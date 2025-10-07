nome = str(input('Qual o seu nome? '))

if nome == 'Evelyn':
    print('Que nome bonito!')
elif nome == 'Enzo' or nome == 'Valentina' or nome == 'Ravi':
    print('Seu nome é bem comum no Brasil')
elif nome in 'Ana Jéssica Michele':
    print('Que nome feminino bonito!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))