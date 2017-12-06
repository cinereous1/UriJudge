#!/usr/bin/python3

nota = float(input().strip())
print("NOTAS: ")
print("{} nota(s) de R$ 100.00".format(int(nota // 100)))
aux = nota % 100
print("{} nota(s) de R$ 50.00".format(int(aux // 50)))
aux %= 50
print("{} nota(s) de R$ 20.00".format(int(aux // 20)))
aux %= 20
print("{} nota(s) de R$ 10.00".format(int(aux // 10)))
aux %= 10
print("{} nota(s) de R$ 5.00".format(int(aux // 5)))
aux %= 5
print("{} nota(s) de R$ 2.00".format(int(aux // 2)))
aux %= 2

print("MOEDAS: ")
print("{} moeda(s) de R$ 1.00".format(int(aux // 1.0)))
aux %= 1.0
print("{} moeda(s) de R$ 0.50".format(int(aux // 0.50)))
aux %= 0.50
print("{} moeda(s) de R$ 0.25".format(int(aux // 0.25)))
aux %= 0.25
print("{} moeda(s) de R$ 0.10".format(int(aux // 0.10)))
aux %= 0.10
print("{} moeda(s) de R$ 0.05".format(int(aux // 0.05)))
aux %= 0.05
print("{} moeda(s) de R$ 0.01".format(int(aux // 0.01)))


