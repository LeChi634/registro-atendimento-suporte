while True:
    try:
        opcao = int(input("\n=== SISTEMA DE SUPORTE TI ===\n"
                "1 - Problema de Internet\n"
                "2 - Computador Lento\n"
                "3 - Erro de Software\n"
                "4 - Outro\n"))

        match opcao:
            case 1:
                tipo = "Problema de internet"
            case 2:
                tipo = "Computador lento"
            case 3:
                tipo = "Erro de software"
            case 4:
                tipo = "Outro"
            case _:
                print("Opção inválida. Digite apenas números de 1 a 4.")
                continue
        break

    except ValueError:
        print("Entrada inválida. Digite apenas números de 1 a 4.")

nome = input("Nome do usuário: ")
setor = input("Setor: ")
descricao = input("Descreva o problema: ")

with open("registros_suporte.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("=== NOVO ATENDIMENTO ===\n")
    arquivo.write(f"Usuário: {nome}\n")
    arquivo.write(f"Setor: {setor}\n")
    arquivo.write(f"Tipo: {tipo}\n")
    arquivo.write(f"Descrição: {descricao}\n")
    arquivo.write("------------------------\n")

print("\nAtendimento registrado com sucesso!")