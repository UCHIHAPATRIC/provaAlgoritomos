from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, cpf: str):
        self.id = id
        self.nome = nome
        self._cpf = cpf  

    @abstractmethod
    def marcarPresenca(self):
        pass

    def matricular(self):
        print(f"{self.nome} foi matriculado.")
