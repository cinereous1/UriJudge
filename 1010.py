#!/usr/bin/python3

arr = []
for i in range(2):
    val = list(map(float, input().strip().split()))
    arr.append(val)

pagar = int(arr[0][1]) * arr[0][2] + int(arr[1][1]) * arr[1][2]
print("VALOR A PAGAR: R$ {:.2f}".format(pagar))
