nome = 'Carlos'
idade = 36
profissao = 'DevOps'

pessoa = {
    'nome': nome,
    'idade': idade,
    'profissao': profissao
}

# Utilizando %
# %s -> string
# %d -> int
# %f -> float
print('Olá, me chamo %s, tenho %d anos de idade e trabalho como %s'
      % (nome, idade, profissao))

# Utilizando format
print('Olá, me chamo {}, tenho {} anos de idade e trabalho como {}'
      .format(nome, idade, profissao))
print('Olá, me chamo {0}, tenho {2} anos de idade e trabalho como {1}'
      .format(nome, profissao, idade))
print('Olá, me chamo {nome}, tenho {idade} anos de idade e trabalho como {profissao}'
      .format(nome=nome, idade=idade, profissao=profissao))
print('Olá, me chamo {nome}, tenho {idade} anos de idade e trabalho como {profissao}'
      .format(**pessoa))

# Utilizando f-string
print(f'Olá, me chamo {nome}, tenho {idade} anos de idade e trabalho como {profissao}')

# formatar string
PI = 3.14159
print(f'Valor de PI: {PI:.2f}')
print(f'Valor de PI: {PI:10.2f}')
