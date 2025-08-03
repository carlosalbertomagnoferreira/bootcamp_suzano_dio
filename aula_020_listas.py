# Exemplos de listas
frutas = ['laranja', 'maca', 'uva']
vazia = []
letras = list('python')
numeros = list(range(10))
carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'Sao Paulo', True]

# acessando itens da lista usando indice
frutas[0]
frutas[1]
frutas[-1]
frutas[-2]

# list comprehension

numeros = [1, 30, 21, 2, 9, 65, 34]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

pares = [numero for numero in numeros if numero % 2 == 0]

quadrado = [numero ** 2 for numero in numeros]
