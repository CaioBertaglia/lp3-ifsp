# 1. números

# int
idade = 20

# float
altura = 1.6

# complex
#cálculos com números complexos
numero_complexo = 1 + 2j

# 2. Booleano
verdade = True
mentira = False

# 3. Sequencias 
# str, list, tuple, set, dict

# str
# conjunto de caracteres
nome = "Joao da Silva"
nome = 'Maria da Silva'

# str de múltiplas linhas
frase = """
Olá Mundo!
Parabéns Amigo
"""

# interpolação de str

# f-strings
nome = 'Maria'
idade = 78
mensagem = f'{nome} é uma pessoa legal! Ela tem {idade} anos'

# char
# não existe
# usar str de tamanho 1
letra = 'A'

# Como acessar os caracteres de uma str?
nome = 'Silvio Santos'
print(nome[2])

# Métodos de str
print(nome.upper())
print(nome.capitalize())
print(nome)

# list
# lista de valores
# permitir diferentes tipo de dados na mesma lista

habilidades = ['python', 'java', 'javascript']
print(habilidades[1]) # java

for habilidade in habilidades:
    print("Teste")
    print(habilidade)

# adiciona no final da lista
habilidades.append('html') #  'python", 'java', 'javascript, 'html'

#adiciona em uma posição
habilidades.insert(1, "css") # 'python', 'css, 'java', 'javascript', 'html'

# remover
habilidades.remove('css')

# tuple
# "lista" de valores
# não pode ser alterada
# sim, nao, talvez
opcoes = ('sim', 'nao', 'talvez')
raca_rpg = ('humano', 'elfo', 'orc')

def estatistica_notas(notas):
     maior = max(notas)
     menor = min(notas)
     media = sum(notas) / len(notas)
     return maior, menor, media

notas = [10.0, 3.5, 7.8]
estatistica = estatistica_notas(notas)
print(estatistica)

#desempacotar uma tupla
maior, menor, media = estatistica_notas(notas) 
print(maior, menor, media)

# set
#conjunto de valores
#não é indexado
#permite elementos duplicados
habilidades = {'java', 'python'}
habilidades.add('java')
print(habilidades)

for habilidade in habilidades:
     print(habilidades)

# dict
# palavra -> definicao
# chave -> valor
# key -> value

nome = "Silvio"
idade = 89
patrimonio = 2000000
altura = 1.7

pessoa = {
     'nome': 'Silvio',
     'idade': 89,
     'patrimonio': 2000000,
     'altura': 1.7
}

print(pessoa[nome])
print(pessoa[idade])
print(pessoa[patrimonio])
print(pessoa[altura])

# None
# variaveis qie serão inicializadas em tempo de execução
# retorno de função
# parametros de função
nulo = None