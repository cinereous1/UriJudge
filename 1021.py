#!/usr/bin/python3

cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

placeholder = real = float(input().strip())
print("NOTAS: ")
for i in range(len(cedulas)):
    placeholder = real // cedulas[i]
    print("{} nota(s) de R$ {:.2f} ". format(int(placeholder), cedulas[i]))
    real %= cedulas[i]

print("MOEDAS: ")
for i in range(len(moedas)):
    placeholder = real // moedas[i]
    print("{} moeda(s) de R$ {:.2f}".format(int(placeholder), moedas[i]))
    real %= moedas[i]

