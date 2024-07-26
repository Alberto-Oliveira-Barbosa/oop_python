from src.pessoa import Pessoa
from src.abstract_pessoa import AbstractPessoa
from src.funcionario import Funcionario
from src.gerente import Gerente

funcionario = Funcionario('Alberto', 36, '2023-01-02', 'Analista 1')

# Acessando diretamente os atributos da classe
print(funcionario.nome)
print(funcionario.idade)

# como o atributo está privado na classe ele não pode ser acessado diretamente 
try:
    print(funcionario.__data_contratacao)
except AttributeError:
    print(f'O Atributo __data_contratacao é privado e por isso não pode ser acessado')

# mas pode ser acessado com um método da Classe
funcionario.mostrar_contratacao()

# os acessos a atributos privados pode ser feito através da criação de propriedades e setters na classe
print(f'Acessando a propert data_contratacao que retorna o valor do atributo __data_contratacao: {funcionario.data_contratacao}')

# a vantagem do propert é que com ele podemos visualizar o seu valor mas não podemos alterá-lo:
try:
    funcionario.data_contratacao = '2024-01-02'
except AttributeError:
    print('A propert data_contratacao é somente LEITURA')

print(f'Acessando a propriedade cargo: {funcionario.cargo}')

# alterando para Analista 2
funcionario.cargo = 'Analista 2'
print(f'Acessando a propriedade cargo depois de alterada: {funcionario.cargo}')



# não é uma boa prática que a classe Pessoa possa ser instanciada diretamente:
pessoa = Pessoa('Pessoa', 30)
print(f'Classe Pessoa instanciada diretamente: {pessoa.nome}')
print(pessoa.idade)

# o ideal é que as classes abstratas não sejam instanciadas diretamente
# para efeito de exemplo a classe Gerente usa uma classe abstrata baseada na classe Pessoa
# normalmente uma classe abstrata possui métodos abstratos que devem ser implementados em suas subclasses
# isso já garante que ela não vai ser instanciada fora de uma subclasse, mas como a Classe AbstractPessoa não possui métodos 
# abstratos, esse check será feito a partir de uma validação dentro do método construtor
try:
    classe_abstrata = AbstractPessoa('Gerente 1', 40)
    print(classe_abstrata)
except Exception as error:
    print(error)

# usando a Subclasse Gerente que herda de AbstractPessoa
gerente = Gerente('Gerente 2', 40, '2020-04-22', 'Gerente Geral')
print(f'Classe Gerente: {gerente.nome}')