#!/usr/bin/python3

import math

l1 = list(map(float, input().strip().split()))
l2 = list(map(float, input().strip().split()))

x1, y1 = l1
x2, y2 = l2

distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print("{:.4f}".format(distancia))
