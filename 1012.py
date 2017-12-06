#!/usr/bin/python3

val = list(map(float, input().strip().split()))

print("TRIANGULO = {:.3f}".format(val[0] * val[2] / 2))
print("CIRCULO = {:.3f}".format(val[2] ** 2 * 3.14159))
print("TRAPEZIO = {:.3f}".format((val[0] + val[1]) * val[2] / 2))
print("QUADRADO = {:.3f}".format(val[1] ** 2))
print("RETANGULO = {:.3f}".format(val[0] * val[1]))
