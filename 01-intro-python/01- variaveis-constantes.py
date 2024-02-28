# Indentificadores
# letra, numero e _
# nao pode ser palavra reservada: if, None, True,False
# case sensitive
nome = "Pedro"
Nome = "Pedro"

# variaveis
# tudo em minusculo
# separador _
# snake_case
idade = 20
pesoa_fisica = "Marcio"
pessoa_juridica = 'Paula LTDA'
imposto_renda = 2200.45

# E o tipo?
# Java
# String nome = "Pedro"
# int idade = 20
# No python temos inferência de tipo
# O tipo será definido com base no valor (literal)
idade = 20 # int
nome = "Pedro" # str

# Constantes
# Não exite constante em python
# Convenção: nome em maiúsculo
PI = 3.14

# Comentários de uma unica linha

'''
Comentário de
mútiplas linhas
'''

# docstring (comentário de documentação)
# documentar classe, módulos, funções, ...

 static somar(double numero1, double numero2) {
    return numero1 + numero2
 }

def somar(numero1, numero2):
    '''
    Função que soma dois números
    :param numero1: primeiro número
    :param numero2: segundo número
    :return: a soma dos números
    '''
    return numero1 + numero2


