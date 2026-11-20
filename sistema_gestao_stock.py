import json
import os

FICHEIRO = "stock.json"

# Carrega os produtos guardados, se o ficheiro existir.
if os.path.exists(FICHEIRO):
    with open(FICHEIRO, "r", encoding="utf-8") as f:
        produtos = json.load(f)
else:
    produtos = []


def guardar():
    """Guarda a lista de produtos no ficheiro JSON."""
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)


def procurar(nome):
    """Procura um produto pelo nome."""
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None


while True:
    print("\n=== SISTEMA DE GESTÃO DE STOCK ===")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Registar entrada")
    print("4. Registar saída")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ").strip()

        if not nome:
            print("O nome não pode ficar vazio.")
            continue

        if procurar(nome):
            print("Esse produto já está cadastrado.")
            continue

        try:
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço por unidade (MT): "))

            if quantidade < 0 or preco < 0:
                print("A quantidade e o preço não podem ser negativos.")
                continue

            produtos.append({
                "nome": nome,
                "quantidade": quantidade,
                "preco": preco
            })
            guardar()
            print("Produto cadastrado com sucesso!")

        except ValueError:
            print("Digite números válidos para quantidade e preço.")

    elif opcao == "2":
        if not produtos:
            print("Ainda não existem produtos cadastrados.")
        else:
            print("\n--- LISTA DE PRODUTOS ---")
            for p in produtos:
                print(f"Produto: {p['nome']} | Stock: {p['quantidade']} | Preço: {p['preco']:.2f} MT")

    elif opcao == "3":
        nome = input("Nome do produto: ").strip()
        produto = procurar(nome)

        if produto:
            try:
                quantidade = int(input("Quantidade a adicionar: "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero.")
                else:
                    produto["quantidade"] += quantidade
                    guardar()
                    print("Entrada registada com sucesso!")
            except ValueError:
                print("Digite uma quantidade válida.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        nome = input("Nome do produto: ").strip()
        produto = procurar(nome)

        if produto:
            try:
                quantidade = int(input("Quantidade a retirar: "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero.")
                elif quantidade > produto["quantidade"]:
                    print("Stock insuficiente!")
                else:
                    produto["quantidade"] -= quantidade
                    guardar()
                    print("Saída registada com sucesso!")
            except ValueError:
                print("Digite uma quantidade válida.")
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        print("Programa encerrado. Até breve!")
        break

    else:
        print("Opção inválida. Tente novamente.")
