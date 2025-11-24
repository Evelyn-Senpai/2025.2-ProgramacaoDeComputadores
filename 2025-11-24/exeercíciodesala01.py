import sys
valores = list()
while True:
    try:
        valor = int(input('Informe um valor: '))
        if valor > 0:
            valores.append(valor)
        elif valor < 0:
            print('O valor deve ser um número positivo')
        else:
            print(f'A lista ficou {valores}')
            break
    except ValueError:
        print('O valor deve ser um número inteiro!')
    except Exception as ERRO:
        print(f'{ERRO}')
    else:
        continue