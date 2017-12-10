#!/usr/bin/python3

# Q1 = x e y positivos
# Q2 = x negativo e y positivo
# Q3 = x e y negativos
# Q4 = x positivo e y negativo

x, y = input().strip().split()
x, y = [ float(x), float(y) ]

if (x == 0 and y == 0):
    print("Origem")
elif (y == 0):
    print("Eixo X")
elif(x == 0):
    print("Eixo Y")
elif(x > 0 and y > 0):
    print("Q1")
elif(x < 0 and y > 0):
    print("Q2")
elif(x < 0 and y < 0):
    print("Q3")
else:
    print("Q4")
