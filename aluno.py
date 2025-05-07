from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id: int, nome: str, cpf: str, matricula: str):
        super().__init__(id, nome, cpf)
        self.__matricula = matricula 

    def marcarPresenca(self):
        print(f"Presença marcada para o aluno {self.nome}.")

    def matricular(self):
        print(f"Aluno {self.nome} com matrícula {self.__matricula} foi matriculado.")

    

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
