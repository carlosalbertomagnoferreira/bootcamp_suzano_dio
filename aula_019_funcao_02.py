def cadastrar_carro_simples(ano, modelo, marca, placa):
    print(f'{ano}, {modelo}, {marca}, {placa}')

def cadastrar_carro_posicional_(ano, modelo, /, *, marca, placa):
    print(f'{ano}, {modelo}, {marca}, {placa}')

cadastrar_carro_simples(2020, '208', 'Peugeot', 'qwu-5h95')

cadastrar_carro_posicional_(2020, '208', marca='Peugeot', placa='qwu-5h95')

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def operacao(a, b, operador):
    return operador(a, b)

soma = operacao(10, 20, somar)
print(soma)

mult = operacao(10, 20, multiplicar)
print(mult)



def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(f'{modelo}, {ano}, {placa}, {marca}, {motor}, {combustivel}')


criar_carro('208', 2020, 'abc 123', 'peugeot', '1.2', 'flex')

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

