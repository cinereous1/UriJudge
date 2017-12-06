#!/usr/bin/python3

input()
sal = float(input().strip())
vendas_mes = float(input().strip())

print("TOTAL = R$ {:.2f}".format(sal + vendas_mes * 15 / 100))
