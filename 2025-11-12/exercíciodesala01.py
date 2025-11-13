'''
   Exemplo 01: Programa para contar quantas vogais existem em uma string 
   fornecida pelo usuário.
'''
texto = str(input('Digite uma palavra: ')).upper().strip()
vogais = 'AEIOU'
quantidade = 0
for letra in texto:
    if letra in vogais:
        quantidade += 1
print(f'Em {texto} tem {quantidade} vogais')