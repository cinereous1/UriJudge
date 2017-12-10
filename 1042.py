numeros = input().strip().split()
numeros = list(map(int, numeros))

numeros_ordem = numeros[:]
numeros.sort()

for numero in numeros:
    print(numero)
print()

for numero in numeros_ordem:
    print(numero)
