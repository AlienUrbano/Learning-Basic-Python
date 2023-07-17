import keyboard

while True: 

    num = int(input("digite um numero para verificar se é par ou impar: "))
    if num %2 == 0:
        print("O numero:", num, "é par")
    else:
        print("O numero:", num, "é impar")
    recomecar = input("aperte qualquer tecla para começar de novo: ")
    if recomecar == keyboard.is_pressed:
        continue