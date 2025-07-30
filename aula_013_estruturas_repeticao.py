VOGAIS = 'AEIOU'

palavra = 'Python'

# utilizando iteravel
for letra in palavra:
    if letra.upper() in VOGAIS:
        print(f'{letra} ', end='')
else:
    print()
    print('Fim do laço for')

# utilizando funçao built-in python
for i in range(1, 11):
    print(f'{i}', end = ' ')

# while
opcao = ''

while opcao != 0:
    opcao = int(input('[1] Sacar\n[2] Extrato\n[0] Sair'))
    if opcao == 1:
        print('Saque selecionado')
    elif opcao == 2:
        print('Extrato selecionado')
else:
    print('Sainda do while')

# break
while True:
    numero = int(input('Informe um numero: '))
    if numero == 10:
        break
    print(f'Numero: {numero}')

for numero in range(100):
    if numero == 11:
        break
    print(numero)

# continue
for i in range(10):
    if i == 5:
        continue
    print(i)
    