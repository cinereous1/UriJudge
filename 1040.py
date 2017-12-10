#!/usr/bin/python3

notas = input().split()
notas = list(map(float, notas))

media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3]) / 10

if(media >= 5.0 and media < 7.0):
    print("Media: {:.1f}".format(media))
    print("Aluno em exame.")

    nota_exame = float(input())

    print("Nota do exame: {:.1f}".format(nota_exame))

    nova_media = (media + nota_exame) / 2

    print("Aluno {}.".format("aprovado" if (nova_media > 5.0) else "reprovado"))
    print("Media final: {:.1f}".format(nova_media))
elif(media >= 7.0):
    print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")
else:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")
