from aluno import Aluno

def main():
    print("=== Cadastro de Aluno ===")
    try:
        id = int(input("Digite o ID para o aluno: "))
        nome = input("Digite o nome do aluno: ")
        cpf = input("Digite o CPF do aluno: ")
        matricula = input("Digite a matrícula para o aluno: ")

        aluno1 = Aluno(id, nome, cpf, matricula)

        print("\n--- Resultado ---")
        aluno1.marcar_presenca()
        aluno1.matricular()
        print("Matrícula atual:", aluno1.matricula)

        nova_matricula = input("Deseja alterar a matrícula? Digite a nova matrícula (ou pressione Enter para manter): ")
        if nova_matricula.strip():
            aluno1.matricula = nova_matricula
            print("Matrícula atualizada:", aluno1.matricula)
        else:
            print("Matrícula mantida:", aluno1.matricula)

    except ValueError:
        print("Erro: ID deve ser um número inteiro.")

if __name__ == "__main__":
    main()
