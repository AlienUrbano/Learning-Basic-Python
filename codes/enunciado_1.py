"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

#programa 1

"""
num= input("Digite um número inteiro: ")

if num.isdigit():
    num =int(num)
    if num %2 ==0:
        print(f"O numero: {num} é par")
    else:
        print(f"O numero: {num} é impar")
else:
    print("isso não é um número.")
"""

#programa 2
"""
hora= input("Digite a hora em números inteiros de 0 à 23: ")

if hora.isdigit():
    hora =int(hora)
    if hora >0 and hora <= 11 :
        print("Bom dia!")
    elif hora >11 and hora <= 17:
        print("Boa Tarde!")
    elif hora >17 and hora <= 23:
        print("Boa noite!")
    else:
        print("Essa hora não existe!")    
else:
    print("isso não é um número.")

"""

#programa 3
"""
nome= input("Digite seu nome: ")
tamanho_nome = len(nome)
nome_curto = tamanho_nome <= 4
nome_normal = tamanho_nome >4 and tamanho_nome <=6

if nome_curto :
    print("Seu nome é curto")
elif nome_normal:
    print("Seu nome é normal")
else:
    print("que nome grande!")
"""