saldo = 1000

def sacar(valor):
    if valor <= saldo:
        print('Saque efetuado com sucesso!')
    else:
        print('Saldo insuficiente')
    print('Obrigado por ser nosso cliente')

sacar(100)

sacar(2000)
