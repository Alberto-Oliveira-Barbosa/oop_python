from src.abstract_pessoa import AbstractPessoa

class Gerente(AbstractPessoa):
    def __init__(self,nome, idade, data_contratacao, cargo):
        super().__init__(nome, idade)
        self.__data_contratacao = data_contratacao
        self.__cargo = cargo

    @property
    def data_contratacao(self):
        return self.__data_contratacao
    
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
        