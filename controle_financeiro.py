import csv
import os

def criar_ou_abrir_arquivo():
    arquivo = "registros.csv"
    if not os.path.exists(arquivo):
        with open(arquivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Data", "Descrição", "Valor"])
    return arquivo

def adicionar_registro(arquivo, data, descricao, valor):
    with open(arquivo, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([data, descricao, valor])
    print("Registro adicionado com sucesso!")

def exibir_registros(arquivo):
    with open(arquivo, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def menu():
    arquivo = criar_ou_abrir_arquivo()

    while True:
        print("\nOpções:")
        print("1. Adicionar Registro")
        print("2. Exibir Registros")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            data = input("Data (DD/MM/AAAA): ")
            descricao = input("Descrição: ")
            valor = input("Valor: ")
            adicionar_registro(arquivo, data, descricao, valor)
        elif escolha == "2":
            exibir_registros(arquivo)
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
