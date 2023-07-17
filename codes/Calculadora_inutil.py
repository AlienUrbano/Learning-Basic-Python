import random
import keyboard

while True:
    print("Bem  vindo a calculadora mais ínutil do planeta, onde todos os números e operações são randomizados! \n")
    iniciar = input("Digite Qualquer tecla para gerar os resultados: \n")
    
    if keyboard.is_pressed:

        num1 = random.randint(1,99)
        num2 = random.randint (1,99)
        numOP = random.randint(1,4)
        soma = num1 + num2 
        sub = num1 - num2 
        mult = num1 * num2
        div = num1 / num2

        if numOP == 1:
            print ("A soma de " , num1 , "+" , num2, "é = " , soma)
        elif numOP == 2:
            print("A subtração de ", num1 ,"-" ,num2 ,"é = ", sub)
        elif numOP == 3:
            print ("A multiplicação de ", num1 ,"*" , num2 ,"é = ", mult)
        else:
            print ("A divisão de ", num1, "/", num2 ,"é = ",div)

    continuar = input("Aperte qualquer tecla começar de novo")
    if continuar == keyboard.is_pressed:
        
        continue

