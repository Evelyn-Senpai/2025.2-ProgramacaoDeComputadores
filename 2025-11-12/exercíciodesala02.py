'''
   Exemplo 02: Programa para contar quantas palavras existem em uma frase
   fornecida pelo usuário.
'''
texto = str(input('Digite uma palavra: ')).split()
quantidade = 0
for palavra in texto:
    quantidade += 1
print(f'Em {texto} tem {quantidade} palavras')