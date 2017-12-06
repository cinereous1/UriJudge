#!/usr/bin/python3

import math

a, b, c = input().strip().split()
a, b, c = [ float(a), float(b), float(c) ]


if (a == 0.0):
    print("Impossivel calcular")
else:
    try:
        delta = b ** 2 - 4 * a * c
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("R1 = {:.5f}\nR2 = {:.5f}".format(x1, x2))
    except:
        print("Impossivel calcular")
