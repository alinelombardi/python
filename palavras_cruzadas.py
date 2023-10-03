grade_palavras_cruzadas = [
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
]

pistas_across = {
    1: "Um pássaro que canta de manhã",
    4: "Oposto de sim",
    7: "Um grande felino",
    10: "Ferramenta usada para cavar"
}

pistas_down = {
    1: "Um corpo celeste que orbita a Terra",
    2: "Uma bebida quente com cafeína",
    3: "O que você faz quando está com fome",
    4: "Oposto de alto"
}

def exibir_grade_palavras_cruzadas(grade):
    for linha in grade:
        print(" ".join(linha))

def jogar_palavras_cruzadas():
    print("Bem-vindo ao jogo de palavras cruzadas!")
    exibir_grade_palavras_cruzadas(grade_palavras_cruzadas)
    print("\nPistas ACROSS:")
    for numero, pista in pistas_across.items():
        print(f"{numero}. {pista}")
    print("\nPistas DOWN:")
    for numero, pista in pistas_down.items():
        print(f"{numero}. {pista}")

if __name__ == "__main__":
    jogar_palavras_cruzadas()
