import sys
numero_de_inscritos = list(range(10))
contador = 0
for inscritos in numero_de_inscritos:
    print("engajamento é bom")
    contador+=1
    if contador == numero_de_inscritos:
        sys.exit()
    else:
        continue