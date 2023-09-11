# STRING

# Em uma string é delimitada por aspas simples, duplas ou triplas:
# ' nome '
# " nome "
# """ nome """
# ''' nome '''
# Em uma variável do tipo str, é possível armazenar:
# letras, números, espaços, pontuação e diversos símbolos

# Metos para tratar string

# UPPER
# Transforma todas em maiúsculas

curso = 'Engenharia de Software'
print(curso.upper())

# ENGENHARIA DE SOFTWARE

# LOWER
# Transforma todas em minúsculas

curso = 'Engenharia de Software'
print(curso.lower())

# engenharia de software

# SPLIT
# Quebra a string em substrings

curso = 'Engenharia de Software'
print(curso.split())

# ['Engenharia', 'de', 'Software']

#===========================================================================

# LISTAS
# Listas são sequências MUTÁVEIS, normalmente usadas para armazenar
# coleções de itens homogêneos.
# Uma lista pode ser criada de algumas maneiras, tais como:

# []
# [a], [a,b,c]
# [x for x in interable]
# list() ou list(iterable)
#   Ex:
#   list('abc') retorna [a,b,c]
#   list('123') retorna [1,2,3]
#   list() retorna []

#===========================================================================

# TUPLAS
# Tuplas são sequências IMUTÁVEIS, tipicamente usadas para armazenar
# coleções de itens heterogêneos.
# Elas são aplicadas também quando é necessário utilizar uma sequência imutável
# de dados homogêneos. Uma tupla pode ser criada de algumas maneiras, tais como:

# ()
# a,b,c ou (a,b,c)
# tuple() ou tuple(iterable)
#   Ex:
#       tuple('abc') retorna ('a','b','c')
#       tuple([1,2,3]) retorna (1,2,3)
#       tuple() retorna ()

# Atenção!
# Note que o uso das vírgulas é o que gera a tupla, e não o uso de parênteses.
# Os parênteses são opcionais, exceto no caso em que queremos
# gerar uma tupla vazia.

#===========================================================================

# RANGE

# O tipo range representa uma sequência imutável de números e frequentemente
# é usado em loops de um número específico de vezes, como o for.

# Nesse caso, a sequência começará em 0 e será incrementada de uma unidade até
# o limite do parâmetro passado (exclusive).
# Ex:
#       range(3) retorna (0,1,2)

# Pode informar o inicio e o fim
#       range(2,7) retorna (2,3,4,5,6)

# Pode informar o inicio, fim e o valor incrementador
#       range(2,9,3) retorna (2,5,8)



