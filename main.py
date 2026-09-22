ARQUIVO = "medicamentos.txt"


# Carrega os medicamentos salvos no arquivo
def carregar_medicamentos():
    medicamentos = []

    arquivo = open(ARQUIVO, "r", encoding="utf-8")

    for linha in arquivo:
        linha = linha.strip()

        if linha != "":
            dados = linha.split(";")

            medicamento = {
                "nome": dados[0],
                "categoria": dados[1],
                "quantidade": int(dados[2])
            }

            medicamentos.append(medicamento)

    arquivo.close()

    return medicamentos

# Salva todos os medicamentos no arquivo
def salvar_medicamentos(medicamentos):
    arquivo = open(ARQUIVO, "w", encoding="utf-8")

    for medicamento in medicamentos:
        linha = (
            medicamento["nome"] + ";"
            + medicamento["categoria"] + ";"
            + str(medicamento["quantidade"]) + "\n"
        )

        arquivo.write(linha)

    arquivo.close()

    # Cadastra um novo medicamento
def cadastrar_medicamento(medicamentos):
    print("\n--- CADASTRAR MEDICAMENTO ---")

    nome = input("Nome do medicamento: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade em estoque: "))

    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }

    medicamentos.append(medicamento)

    print("Medicamento cadastrado com sucesso!")

    return medicamentos

# Listar todos os medicamentos
def listar_medicamentos(medicamentos):
    print("\n--- LISTA DE MEDICAMENTOS ---")

    if len(medicamentos) == 0:
        print("Nenhum medicamento cadastrado.")
    else:
        numero = 1

        for medicamento in medicamentos:
            print("\nMedicamento", numero)
            print("Nome:", medicamento["nome"])
            print("Categoria:", medicamento["categoria"])
            print("Quantidade:", medicamento["quantidade"])

            numero = numero + 1


# Busca um medicamento pelo nome
def buscar_medicamento(medicamentos, nome_busca):
    resultado = []

    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome_busca.lower():
            resultado.append(medicamento)

    return resultado

# Programa principal
def main():
    medicamentos = carregar_medicamentos()

    while True:
        print("\n==============================")
        print(" SISTEMA DE MEDICAMENTOS")
        print("==============================")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Buscar medicamento")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            medicamentos = cadastrar_medicamento(medicamentos)

        elif opcao == "2":
            listar_medicamentos(medicamentos)

        elif opcao == "3":
            nome = input("Digite o nome do medicamento: ")

            resultado = buscar_medicamento(medicamentos, nome)

            if len(resultado) == 0:
                print("Medicamento não encontrado.")
            else:
                print("\n--- MEDICAMENTO ENCONTRADO ---")

                for medicamento in resultado:
                    print("Nome:", medicamento["nome"])
                    print("Categoria:", medicamento["categoria"])
                    print("Quantidade:", medicamento["quantidade"])

        elif opcao == "4":
            salvar_medicamentos(medicamentos)

            print("Dados salvos com sucesso.")
            print("Programa encerrado.")

            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


main()



    





