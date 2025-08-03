from datetime import datetime


def menu():
    menu = '''
Selecione a operacao desejada:
[1] - Criar Usuario
[2] - Criar Conta
[3] - Listar Contas
[4] - Deposito
[5] - Saque
[6] - Extrato
[7] - Sair
=> '''
    return menu
    

def cadastrar_usuario():
    cpf = input('Informe o CPF: ')
    nome = input('Informe o nome completo: ')
    usuario = dict(cpf=cpf, nome=nome)
    return usuario


def buscar_usuario(cpf, usuarios):
    usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario


def cadastrar_conta(cpf, numero_conta):
    agencia = '0001'
    cpf = cpf
    conta = dict(agencia=agencia, conta=numero_conta, cpf=cpf, saldo=0)
    return conta


def buscar_conta(cpf, contas, usuarios):
    usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    if usuario:
        conta = [conta for conta in contas if conta['cpf'] == cpf]
        if conta:
            return True, conta
        else:
            return True, False
    else:
        return False, False


def listar_contas(contas):
    for conta in contas:
        print(f"Agencia: {conta['agencia']}, Conta: {conta['conta']}, CPF: {conta['cpf']}, Saldo: {conta['saldo']}")


def busca_conta_numero(numero_conta, contas):
    conta = [conta for conta in contas if numero_conta == conta['conta']]
    return conta


def realizar_deposito(numero_conta, valor_deposito, contas):
    conta = busca_conta_numero(numero_conta, contas)
    if conta:
        conta[0]['saldo'] += valor_deposito
        print('Deposito realizado com sucesso\n')
    else:
        print('Conta não encontrada\n')


def realizar_extrato(numero_conta, extrato_contas, contas):
    conta = busca_conta_numero(numero_conta, contas)
    if conta:
        print(' INICIO EXTRATO '.center(25, '#'))
        for extrato in extrato_contas[numero_conta]:
            print(extrato)
        print(f'O saldo em conta é de R$ {conta[0]["saldo"]:.2f}')
        print(' FIM EXTRATO '.center(25, '#'))
    else:
        print('Conta não entrada')


def main():
    usuarios = []
    contas = []
    LIMITE_SAQUE = 500
    LIMITE_DIARIO = 3
    LIMITE_OPERACOES_DIA = 10
    extrato_contas = {}
    numero_contas = 1

    while True:
        operacao = int(input(menu()))
        if operacao == 1:
            print('Selecionado Criar Usuario:\n')
            usuario = cadastrar_usuario()
            usuario_existe = buscar_usuario(usuario['cpf'], usuarios)
            if usuario_existe:
                print('Usuario já cadastrado')
            else:
                usuarios.append(usuario)
                print('Usuario cadastrado com sucesso')

        elif operacao == 2:
            print('Selecionado Criar Conta:\n')
            cpf = input('Informe o cpf para cadastro: ')
            conta = cadastrar_conta(cpf, numero_contas)
            usuariob, contab = buscar_conta(cpf, contas, usuarios)
            if usuariob and contab:
                print('Usuario já possui conta')
            elif usuariob and not contab:
                contas.append(conta)
                print('Conta cadastrada com sucesso')
                extrato_contas[numero_contas] = [f'Conta criada em: {datetime.now()}']
                numero_contas += 1
            else:
                print('Usuario não encontrado')

        elif operacao == 3:
            print('Contas cadastradas:\n')
            if len(contas) == 0:
                print('Sem contas cadastradas')
                continue
            listar_contas(contas)

        elif operacao == 4:
            print('Selecionado Deposito\n')
            numero_conta = int(input('Informe o numero da conta: '))
            valor_deposito = int(input('Informe o valor de deposito: '))
            if valor_deposito > 0:
                realizar_deposito(numero_conta, valor_deposito, contas)
                extrato_contas[numero_conta].append(f'DEPOSITO: R$ {valor_deposito} em {datetime.now()}')
            else:
                print('Não é possivel realizar deposito de valor negativo')

        elif operacao == 5:
            print('Selecionado Saque\n')
            numero_conta = int(input('Informe o numero da conta: '))
            valor_saque = int(input('Informe o valor do saque: '))
            conta = busca_conta_numero(numero_conta, contas)
            if conta:
                if valor_saque > 0:
                    if valor_saque > LIMITE_SAQUE:
                        print('Valor limite para saque excedido')
                        continue
                    # elif saques == LIMITE_DIARIO:
                    #     print('Limite de saques excedido')
                    elif valor_saque > conta[0]['saldo']:
                        print('Saldo insuficiente para saque')
                    elif conta[0]['saldo'] >= valor_saque and valor_saque <= LIMITE_SAQUE:
                        conta[0]['saldo'] -= valor_saque
                        print('Saque efetuado')
                        extrato_contas[numero_conta].append(f'SAQUE: R$ {valor_deposito} em {datetime.now()}')
                        # extrato_str += f'Saque: R$ {valor:.2f}\n'
                        # saques += 1
                else:
                    print(f'Não é possivel realizar saque negativo')
            else:
                print('Conta informada não encotrada')


        elif operacao == 6:
            print('Selecionado Extrato\n')
            numero_conta = int(input('Informe a conta que deseja o extrato: '))
            realizar_extrato(numero_conta, extrato_contas, contas)

        elif operacao == 7:
            print('Selecionado Sair')
            break

        else:
            print('Operacao invalida')


main()
