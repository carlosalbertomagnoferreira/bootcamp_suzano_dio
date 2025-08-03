''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    
    saldo = sum(transacoes)

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return f'Saldo: R$ {saldo:.2f}'
    

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

valores = ''
for valor in entrada_usuario.split(','):
    valor = eval(valor)
    valores += f'{valor} '

entrada_usuario = ','.join(valores.split( ))

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)