excelente = 0
ruim = 0

for i in range(50):
    print("\nEntrevistado", i + 1)

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n===== RESULTADO DA PESQUISA =====")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)