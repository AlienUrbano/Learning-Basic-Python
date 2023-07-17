import sys

while True: 
    try: 
        h = (input("digite sua altura em metros (1.40m ~2.40m) :"))
        h_float = float(h)  
        h_valid = h_float >= 1.40 and h_float <=2.40
        peso_ideal_m = (72.7*h_float) - 58
        peso_ideal_f = (62.1*h_float) - 44.7
        
        if h_valid:
                print(f'O peso ideal para homens de {h}m, é de: {peso_ideal_m:.2f}kg')
                print(f'E o peso ideal para mulheres de {h}m, é de: {peso_ideal_f:.2f}kg')

        else:
             print('insira uma altura válida, entre 1.40 e 2.40, tente novamente')
             continue
        
        while True: 
            finalizar = input('Deseja sair ou recomeçar? S ou R :')
            if finalizar.lower() == "s":
                sys.exit()
            elif finalizar.lower() == "r":
                break
            else: 
                 print('Entrada invalida, tente novamente...')
                 continue   
            
    except:
        print('Entrada invalida, utilize "." e não "," , tente novamente')
        continue
