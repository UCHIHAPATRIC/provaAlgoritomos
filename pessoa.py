from abc import ABC, abstractmethod

class Pessoa(ABC):
    """
    Classe abstrata que representa uma pessoa.
    """
    def __init__(self, id: int, nome: str, cpf: str):
        self.id: int = id
        self.nome: str = nome
        self._cpf: str = cpf 

    @abstractmethod
    def marcar_presenca(self) -> None:
        """
        Método abstrato para marcar presença.
        """
        pass

    def matricular(self) -> None:
        print(f"{self.nome} foi matriculado com sucesso.")
