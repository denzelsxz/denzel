notas = []

# cadastrar
def agregar_nota():
    nome = input("Escreva o nome do aluno: ")

    while True:
        nota = float(input("Escreva a nota (0-10): "))
        notas.append(nota)

        print(f"Nota adicionada com sucesso!")

        resposta = input("Deseja adicionar outra nota? (sim/não): ")

        if resposta != "sim":
            break

    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")


# cálculo de média
def calcular_media():
    soma = 0
    maior = 0

    for nota in notas:
        soma += nota
        if nota > maior:
                maior = nota

    divisor = len(notas)

    media = soma / divisor

    print(f"A média é: {media}")
    print(f"A maior nota é: {maior}")

    if media >= 7:
         print("Aprovado!")

    elif media >= 5:
         print("Precisa fazer a substitutiva.")

    else: 
         print("Reprovado!")

agregar_nota()
calcular_media()