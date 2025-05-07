from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, cpf: str):
        self.id: int = id
        self.nome: str = nome
        self._cpf: str = cpf 

    @abstractmethod
    def marcar_presenca(self) -> None:
        pass

    def matricular(self) -> None:
        print(f"{self.nome} foi matriculado com sucesso.")
