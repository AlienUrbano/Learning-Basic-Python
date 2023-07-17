import sys

while True: 
    nome = input("digite seu nome: ")
    sua_idade = input("digite sua idade: ")
    total_caracteres_nome = len(nome)
    # print(f"{sua_idade}, {nome}")

    if nome and sua_idade:
        print(f"Seu nome é: {nome}")
        print(f"Seu nome invertido é: {nome[::-1]}")

        if " " in nome:
            print("Seu nome contém espaços")
             
        else:
            print("Seu nome não contém espaços")

        print(f"O total de caracteres no seu nome é: {total_caracteres_nome}")
        print(f"A letra inicial do seu nome é: {nome[0]}")
        print(f"A ultima letra do seu nome é: {nome[-1]}")


    else:
        print("Você deixou campos vazios, desculpe")
        continue
    
    while True:

        finalizar = input("Deseja recomeçar o programa? [S] sim [N] não: ")
        if finalizar.lower() == "s":
            break  # Sai do loop interno e volta para o início do loop externo
        elif finalizar.lower() == "n":
            sys.exit()  # Sai do loop interno e encerra o programa, o comando Break aqui retornaria para o loop principal, não encerrando.
        else:
            print("Comando inválido. Tente novamente respondendo apenas S ou N.")
