from ast import Str


class User:
    def __init__(self, name : str, cpf : str, birthYear : int):
        self.name = name
        self.CPF = cpf
        self.birthYear = birthYear