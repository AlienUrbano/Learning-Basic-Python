#-*- coding: utf-8 -*-
while True:
    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a segunda nota? "))
    notaTotal = (nota1 + nota2) / 2

    print(notaTotal)
    if notaTotal >= 6:
        print("Você está aprovado!")
    else:
        print("Você está reprovado :(")

    fechar = int(input("Deseja fechar o programa? Digite 1 para fechar, 2 para continuar: "))

    if fechar == 1:
        break