#!/usr/bin/python3

valores = []
for i in range(4):
    valores.append(int(input().strip()))
diff = valores[0] * valores[1] - valores[2] * valores[3]
print("DIFERENCA = {}".format(diff))
