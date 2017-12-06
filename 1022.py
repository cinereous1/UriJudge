#!/usr/bin/python3

from fractions import Fraction

n = int(input().strip())

for i in range(n):
    n1, o1, d1, o3, n2, o2, d2 = input().split()
    if "+" in o3:
        num = int(n1) * int(d2) + int(n2) * int(d1)
        div = int(d1) * int(d2)
    elif "-" in o3:
        num = int(n1) * int(d2) - int(n2) * int(d1)
        div = int(d1) * int(d2)
    elif "*" in o3:
        num = int(n1) * int(n2)
        div = int(d1) * int(d2)
    else:
        num = int(n1) * int(d2)
        div = int(n2) * int(d1)
    
    res = Fraction(num, div)
    print("{}/{} = {}/{}".format(num, div, res.numerator, res.denominator))
