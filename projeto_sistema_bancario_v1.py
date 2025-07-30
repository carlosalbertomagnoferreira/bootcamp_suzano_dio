LIMITE_SAQUE = 500
LIMITE_DIARIO = 3
saldo = 0
extrato_str = ''
saques = 0

menu = '''
Selecione a operacao desejada:
[1] - Deposito
[2] - Saque
[3] - Extrato
[4] - Sair
'''

while True:
    operacao = int(input(menu))
    if operacao == 1:
        print('Selecionado Deposito\n')
        valor = int(input('Digite o valor que deseja depositar: '))
        if valor > 0:
            saldo += valor
            extrato_str += f'Deposito: R$ {valor:.2f}\n'
            print('Depositado realizado')
        else:
            print(f'Deposito invalido, verifique o valor depositado: {valor}')

    elif operacao == 2:
        print('Selecionado Saque\n')
        valor = int(input('Digite o valor que deseja sacar: '))
        if valor > 0:
        
            if valor > LIMITE_SAQUE:
                print('Valor limite para saque excedido')
            elif saques == LIMITE_DIARIO:
                print('Limite de saques excedido')
            elif valor > saldo:
                print('Saldo insuficiente para saque')
            elif saldo >= valor and valor <= LIMITE_SAQUE:
                saldo -= valor
                print('Saque efetuado')
                extrato_str += f'Saque: R$ {valor:.2f}\n'
                saques += 1
        else:
            print(f'Saque invalido, verifique o valor de saque: {valor}')

    elif operacao == 3:
        print('Selecionado Extrato\n')
        print(' INICIO EXTRATO '.center(25, '#'))
        print('Sem operações para extrato' if not extrato_str else extrato_str)
        print(f'O saldo em conta é de R$ {saldo:.2f}')
        print(' FIM EXTRATO '.center(25, '#'))
    elif operacao == 4:
        print('Selecionado Sair')
        break

    else:
        print('Operacao invalida')
