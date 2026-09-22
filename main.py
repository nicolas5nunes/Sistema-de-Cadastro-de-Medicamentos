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




