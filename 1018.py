#!/usr/bin/python3

cedulas = [100, 50, 20, 10, 5, 2, 1]
placeholder = real = int(input().strip())

if (0 < real < 1000000):

    print(real)
    for i in range(len(cedulas)):
        placeholder = real // cedulas[i]
        print("{} nota(s) de R$ {:.2f} ". format(placeholder, cedulas[i]))
        real %= cedulas[i]

# 3l: lista com todas as cedulas em reais, 4l-5l campo de variaveis
# 8l: placeholder recebe a divisão inteira do real divido pelo valor atual da lista em posição i
# 10l: real recebe o modulo dele mesmo pelo valor da cedula na posição i
