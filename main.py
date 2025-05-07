from aluno import Aluno

def main():
    aluno1 = Aluno(1, "Maria João", "123.456.789-00", "20250001")
    aluno1.marcarPresenca()
    aluno1.matricular()

    print("Matrícula atual:", aluno1.get_matricula())
    aluno1.set_matricula("20259999")
    print("Nova matrícula:", aluno1.get_matricula())

if __name__ == "__main__":
    main()
