#!/usr/bin/python3

a, b, c, d = input().strip().split()
a, b, c, d= [ int(a), int(b), int(c), int(d) ]

res = "Valores aceitos" if ((b > c) and (d > a) and (c + d > a + b) and (a >0 and b > 0 and c > 0 and d >0) and (a % 2 ==0)) else "Valores nao aceitos"

print(res)
