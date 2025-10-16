# Crie um programa que leia uma frase qualquer e diga se ela é um POLÍNDROMO, desconsiderando os espaços.

# TIRA OS ESPAÇOS E DEIXA TODOS OS DIGITOS EM MAISCULO PARA NÃO TER PROBLEMA DE COMPARAÇÃO DEPOIS.
frase = str(input('Digite uma frase: ')).strip().upper() 
# SEPARA AS PALAVRAS DE ACORDO COM OS ESPAÇOS.
palavra = frase.split()
# JUNTA TODAS AS PALAVRAS.   
junto = ''.join(palavra)

inverso = ''

# O LENG PARA PEGAR A ÚLTIMA LETRA DE JUNTO( -1 PORQUE ELE NÃO VAI ATÉ A ÚLTIMA ), VAI ATÉ - 1 ( PORQUE A PRIMEIRA NÃO É 1, É 0 ), E VAI VOLTAR DE - 1 EM - 1.
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('\033[33mO inverso de {} é {}'.format(junto, inverso))

if junto == inverso:
    print('\033[32mTemos um POLÍNDROMO'.format(junto, inverso))

else:
    print('\033[31mNÃO temos POLÍNDROMO'.format(junto, inverso))

# ======================================================================

# frase = str(input('Digite uma frase: ')).strip().upper() 

# palavra = frase.split()

# junto = ''.join(palavra)

# inverso = junto[::-1]


# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra]

# print('\033[33mO inverso de {} é {}'.format(junto, inverso))
# if junto == inverso:
#     print('\033[32mTemos um POLÍNDROMO'.format(junto, inverso))

# else:
#     print('\033[31mNÃO temos POLÍNDROMO'.format(junto, inverso))