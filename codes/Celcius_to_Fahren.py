import keyboard 
while True:

    tempC = float(input("insira a temperatura em graus Celcius para converter para Fahren: "))
    tempF = ((tempC *9/5) + 32)
    print("A temperatura ", tempC,"c°", "em Fahren é: ", tempF,"F")
    terminar = input("deseja começar de novo? digite qualquer tecla:  ")
    if terminar == keyboard.is_pressed:
        continue 