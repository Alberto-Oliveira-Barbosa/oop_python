from src.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self,nome, idade, data_contratacao, cargo):
        # usa o contrutor da classe pai
        super().__init__(nome, idade)
        
        # atributos privados
        self.__data_contratacao = data_contratacao
        self.__cargo = cargo

    
    # como o atributo está privado ele ainda assim pode ser usado pela classe pai e suas subclasses
    def mostrar_contratacao(self):
        print('Acessando o atributo __data_contratacao a partir de um método na classe Funcionario: ', self.__data_contratacao)

    
    # para controlar melhor o acesso a atributos privados, podemos usar gets(property) e setters:

    @property
    def data_contratacao(self):
        return self.__data_contratacao
    
    @property
    def cargo(self):
        return self.__cargo
    
    # escrita no atributo __cargo
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
        