# LISTAS (ARRAY) - ESTRUTURA DE DADOS - Usamos [] Colchetes para colocarmos os dados e formar a lista
# ----------------------------------------------------------------------------------------------------------
# Antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com Lista

notas = [7.9, 9.7, 8.2]

# ----------------------------------------------------------------------------------------------------------
# CRIANDO LISTAS
# ----------------------------------------------------------------------------------------------------------

# lista = []  # Lista vazia
# lista = list()  # Outra forma de criar lista
# lista = [26, 'Texto', 3.14159, False]  # Pode colocar diversos tipos de dados: number, string, bool
# lista = [10, [1, 2, 3]]  # Uma lista pode receber outra lista dentro dela, Listas de lista


# ----------------------------------------------------------------------------------------------------------
# INDEXAÇÃO E SLICE (FATIAMENTO)
# ----------------------------------------------------------------------------------------------------------
# Indexação é a forma de acessar um elemento dentro de um índice
# ----------------------------------------------------------------------------------------------------------

lista = [26, 'Texto', 3.14159, False]
print(lista[1])  # Para acessar o elemento que está no índice 1 "Texto"
print(lista[3])
# print(lista[4]) # Quando colocamos um indice que nao existe na lista ele apresenta um erro

print(lista[-1])  # Quando colocamos indice negativo, vai mostra na ordem inversa, ou seja,
# o último elemento e assim por diante


# ----------------------------------------------------------------------------------------------------------
# SLICE (FATIAMENTO)
# ----------------------------------------------------------------------------------------------------------

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])  # Vai começar no indice 0 até o menor que o 3
print(lista[3:6])
print(lista[3:])  # Quando colocamos aprenas um numero ele vai começar dele até o final da lista
print(lista[2:6:2])  # Começa do 2 vai até o 6, pulando de 2 em 2

# ----------------------------------------------------------------------------------------------------------
# ALTERAÇÕES COM FOR
# ----------------------------------------------------------------------------------------------------------
# 1. Ultilizando os próprios elementos da lista
# ----------------------------------------------------------------------------------------------------------

for elemento in lista:
    print(elemento)

# ----------------------------------------------------------------------------------------------------------
# 2. Ultilizando os índices
# ----------------------------------------------------------------------------------------------------------

print('Cpmprimento da lista: ', len(lista))  # len (length) - o comprimento da lista, ou seja, o tamanho da lista

for i in range(len(lista)):  # A lista tem 7 elementos, ele vai imprimir de (0 até 6)
    # print(lista[i]) # vai mostrar 10 50 30 40 25 60 5, ou seja, os valores de cada índice
    print(i)  # vai mostrar 0 1 2 3 4 5 6 ou seja os índices do array

##############################################################################################
# FUNÇÃO EVAL()
# A função eval() recebe uma string, mas trata como um valor numérico.
##############################################################################################

a = '3 * 9'

eval(a)
type(a)
