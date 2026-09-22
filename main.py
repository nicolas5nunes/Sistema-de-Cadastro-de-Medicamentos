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

# Lista todos os medicamentos
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





