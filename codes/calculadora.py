m1 = 0
while True:

    num1 = input(f"Digite um número ou 'mem' para utilizar o ultimo resultado '{m1}': ")
    operacao = input("Digite uma operação '[+],[-],[*], ou [/]' :")
    num2 = input("Digite o segundo número: ")
    
    
    if num1.lower() == "mem":
        num1 = m1    
 
    try: 
        num1 = float(num1)
        num2 = float(num2)
    except:
        print("Esses não são números! reiniciando...")
        continue    
    operacoes_validas = ["+", "-", "*", "/"]
    operacao_valida = operacao in operacoes_validas
      
    if  operacao_valida:
        soma = num1 + num2
        multiplicacao = num1 * num2
        divisao = num1 / num2
        subtracao = num1 - num2
    else:    
        print("Isso não é uma operação válida, tente novamente.")
        continue 
    
   
    if operacao == "+" :
        print(f"A soma de {num1 } + {num2} é = {soma}")
        m1 = soma
    elif operacao == "-" :
        print(f"A subtração de {num1 } - {num2} é = {subtracao}")  
        m1 = subtracao
    elif operacao == "*" :
        print(f"A multiplicação de {num1 } * {num2} é = {multiplicacao}")
        m1 = multiplicacao    
    elif operacao == "/" :
        print(f"A divisão de {num1 } / {num2} é = {divisao}")
        m1 = divisao
                       
    finalizar = input("Deseja finalizar o programa ou realizar outra operação? Digite 'S' de sair ou 'R' de recomeçar:  ") 
    if finalizar.lower() == "s":
        break
    elif finalizar.lower() == "r":
        continue
    else:
        print("Você não digitou uma opção válida, reiniciando...")
        continue
        
    
