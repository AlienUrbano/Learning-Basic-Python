lista_compras = []

# Adicionar itens à lista de compras
def adicionar_item(item, preco_estimado):
    lista_compras.append((item, preco_estimado))
    print(f"{item} foi adicionado à lista de compras.")

# Remover itens da lista de compras
def remover_item(item):
    for i, (nome_item, _) in enumerate(lista_compras):
        if nome_item == item:
            lista_compras.pop(i)
            print(f"{item} foi removido da lista de compras.")
            return
    print(f"{item} não está na lista de compras.")

# Exibir lista de compras com preços estimados
def exibir_lista():
    print("Lista de compras:")
    total = 0
    for index, (item, preco_estimado) in enumerate(lista_compras):
        if preco_estimado:
            total += preco_estimado
            print(f"{index+1}. {item} - Preço Estimado: R$ {preco_estimado:.2f}")
        else:
            print(f"{index+1}. {item} - Preço Estimado indisponível")
    print(f"Total: R$ {total:.2f}")

# Limpar lista de compras
def limpar_lista():
    lista_compras.clear()
    print("A lista de compras foi limpa.")

# Loop principal
while True:
    print("O que você deseja fazer?")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista de compras")
    print("4. Limpar lista de compras")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        preco_estimado = float(input("Digite o preço estimado em R$ (ou deixe em branco para indisponível): "))
        adicionar_item(item, preco_estimado)
    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        remover_item(item)
    elif opcao == "3":
        exibir_lista()
    elif opcao == "4":
        limpar_lista()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
