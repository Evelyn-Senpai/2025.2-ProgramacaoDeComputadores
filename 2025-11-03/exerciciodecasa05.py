'''
   Reescreva o programa a seguir usando o laço FOR.
'''

# # Definição das variáveis
# intMultiplicando = 1
# intMultiplicador = 6

# # Definição do laço de repetição
# # Exibe a tabuada do 6 enquanto o multiplicando for menor ou igual a 10
# while intMultiplicando <= 10:
#    # Cálculo do produto
#    intProduto = intMultiplicador * intMultiplicando
#    # Exibição do resultado
#    print(f'{intMultiplicador} x {intMultiplicando} = {intProduto}')
#    # Incremento do multiplicando
#    intMultiplicando += 1

intMultiplicando = 1
intMultiplicador = 6
for c in range(1, 10+1):
    intProduto = intMultiplicador * intMultiplicando
    print(f'{intMultiplicador} x {intMultiplicando} = {intProduto}')
    intMultiplicando += 1