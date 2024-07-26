from abc import ABC

class AbstractPessoa(ABC):
    def __init__(self, nome, idade):
        if self.__class__ is AbstractPessoa:
            raise TypeError(f"A classe {self.__class__.__name__} não deve ser instanciada diretamente!\nUse a sua subclasse específica")
        self.nome = nome
        self.idade = idade
    


