#!/usr/bin/python3

arr = []
for i in range(3):
    arr.append(input().strip())
arr[0], arr[1], arr[2] = int(arr[0]), int(arr[1]), float(arr[2])

salario = arr[1] * arr[2]

print("NUMBER = {}".format(arr[0]))
print("SALARY = U$ {:.2f}".format(arr[1] * arr[2]))
