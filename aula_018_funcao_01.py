def mensagem():
    print('Ola mundo')

def saudacao(nome):
    print(f'Seja bem vindo {nome}')

def soma(a, b):
    return a + b

def args_kwargs(*args, **kwargs):
    print(args, kwargs)


args_kwargs('a', 'b', 'c', letra='a', numero='1')

