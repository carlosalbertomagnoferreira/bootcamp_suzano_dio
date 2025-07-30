MAIOR_IDADE = 18

idade = int(input('Informe a sua idade: '))

# Checagem de idade para tirar CNH com if simples
if idade >= MAIOR_IDADE:
    print('Pode tirar CNH')

if idade < MAIOR_IDADE:
    print('Não pode tirar CNH')

# Checagem de idade para tirar CNH com if else
if idade >= MAIOR_IDADE:
    print('Pode tirar CNH')
else:
    print('Não pode tirar CNH')

# If aninhado
conta_normal = True
conta_estudante = False

saldo = 1000
cheque_especial = 200

saque = 1200

if conta_normal:
    if saldo >= saque:
        print('Saque efetuado com sucesso')
    elif (saldo + cheque_especial) >= saque:
        print('Saque efetuado com sucesso')
    else:
        print('Saldo insuficiente')

elif conta_estudante:
    if saldo >= saque:
        print('Saque efetuado com sucesso')
    else:
        print('Saldo insuficiente')
else:
    print('Tipo de conta não identificado')

# If ternario
status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'{status} ao realizar o saque')
