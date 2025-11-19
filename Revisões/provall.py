saldo = 0
import sys
while True:
    try:
        opcao = str(input('(C) - Crédito \n(D) - Débito \n(S) - Exibir Saldo \n(X) - Sair Do Programa \nQual operação você deseja realizar? ')).strip().upper()[0]
        if opcao == 'X':
            print('Saindo do programa...')
            print(f'Seu saldo final é {saldo:.2f}')
            sys.exit('Fim do programa')
        elif opcao == 'C':
            print('--- Crédito ---')
            credito = float(input('Qual valor você quer créditar ao seu saldo? R$ '))
            if credito < 0:
                print('O valor deve ser positivo!')
            else:
                print('Crédito efetuado com sucesso!')
                saldo += credito
        elif opcao == 'D':
            print('--- Débito ---')
            debito = float(input('Qual o valor do débito que você deseja realizar? R$ '))
            if debito < 0:
                print('O valor deve ser positivo!')
            elif saldo < debito:
                print('Saldo insuficiente!')
            else:
                print('Débito efetuado com sucesso!')
                saldo -= debito
        elif opcao == 'S':
            print('Exibir saldo')
            print(f'Seu saldo é de {saldo:.2f}')
        else:
            print('Opção inválida, tente novamente...')
    except ValueError:
        sys.exit('ERRO: Informe uma operação!')
    except Exception as ERRO:
        sys.exit(f'ERRO: {ERRO}')
    else:
        continue