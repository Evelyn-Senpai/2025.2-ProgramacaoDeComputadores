'''
String -> Cadeias de caracters
       -> Estrutura de dados homogênea
       -> Cada caracters possui uma posição (índice = index)
'''
strNome = 'Rio Grande do Norte'
print(strNome)
print(strNome[8])
print(strNome[-3])
print(strNome[1:5])
print(strNome[:10])
print(strNome[10:])
strSenha='123Mudar'
strEntrada=input('Digite a senha')
if strEntrada == strSenha:
    print ('OK!!!')
else:
    print ('Erro!!!')