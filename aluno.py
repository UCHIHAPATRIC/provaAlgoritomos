from pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, id: int, nome: str, cpf: str, matricula: str):
        super().__init__(id, nome, cpf)
        self.__matricula: str = matricula

    def marcar_presenca(self) -> None:
        print(f"Presença registrada para o aluno {self.nome}.")

    def matricular(self) -> None:
        print(f"Aluno {self.nome} com matrícula {self.__matricula} foi matriculado com sucesso.")


    
    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, nova_matricula: str) -> None:
        self.__matricula = nova_matricula
