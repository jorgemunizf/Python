# MÉTODOS DE LISTAS - Metodo é uma espécie de função que está atrelada a uma variável

lista = [1, 3, 12, 8, 2]

# ----------------------------------------------------------------------------------------------------------
# APPEND
# ----------------------------------------------------------------------------------------------------------
# Adicionar um elemento no final da lista
# ----------------------------------------------------------------------------------------------------------

print('Antes do append: ', lista)
# [1, 3, 12, 8, 2]

lista.append(3)  # Vai adicionar o número 3 ao final da lista
print('Depois do append: ', lista)
# [1, 3, 12, 8, 2, 3]


# ----------------------------------------------------------------------------------------------------------
# INSERT
# ----------------------------------------------------------------------------------------------------------
# Adiciona um elemento, só que pode escolher quel a posição ele vai ficar
# ----------------------------------------------------------------------------------------------------------

lista.insert(2, 10)  # 1. vai colocar em qual posição ele vai ficar, depois quel elemento vai adicionar
print('Depois do insert: ', lista)  # [1, 3, 10, 12, 8, 2, 3], o 10 foi adicionado na posição 2


# ----------------------------------------------------------------------------------------------------------
# EXTEND
# ----------------------------------------------------------------------------------------------------------
# Quando for unir duas lista em uma só
# ----------------------------------------------------------------------------------------------------------

lista1 = [7, 8, 9]
lista2 = [1, 2, 3]

lista1.extend(lista2)  # vai pegar os elementos do lista2 e colocar no final da lista1

print('Depois de extend: ', lista1)
# Depois de extend:  [7, 8, 9, 1, 2, 3]


# ----------------------------------------------------------------------------------------------------------
# POP
# Vai remover elementos do final da lista ou o elemento que for especificado.
# ----------------------------------------------------------------------------------------------------------

lista4 = [2, 4, 67, 44, 3, 567]

lista4.pop()  # remover o último elemento

print('Lista após do pop: ', lista4)
# Lista após do pop:  [2, 4, 67, 44, 3], removeu o "567" da lista

lista4.pop(2)  # vai remover o índice 2 que é o elemento "67" da lista

print('Lista após o pop(2): ', lista4)
# Lista após o pop(2):  [2, 4, 44, 3, 567]


# ----------------------------------------------------------------------------------------------------------
# REMOVE
# Vai remover o PRIMEIRO ELEMENTO INDICADO
# ----------------------------------------------------------------------------------------------------------

lista = [2, 4, 67, 44, 3, 44, 567]

lista.remove(44)  # Vai remover o primeiro elemento especificado que encontrar "44" da lista.
# Ele vai procurar o elemento dentro da lista e remover

print('Listta após o remove: ', lista)


# ----------------------------------------------------------------------------------------------------------
# COUNT
# Serve para contar  quantas vezes um elemento aparece na lista
# ----------------------------------------------------------------------------------------------------------

lista = [2, 4, 67, 44, 3, 44, 2, 4, 2, 44, 567]

print('Quantidade de 2 na lista: ', lista.count(2))  # Vai contar o quantidade de "2" na lista
# Quantidade de 2 na lista:  3


# ----------------------------------------------------------------------------------------------------------
# INDEX
# Vai te mostrar o primeiro índice encontrado de determinado elemento da lista
# ----------------------------------------------------------------------------------------------------------

lista = [2, 4, 67, 44, 3, 44, 2, 4, 2, 44, 567]

print('Índice do elemento 44: ', lista.index(44))


# ----------------------------------------------------------------------------------------------------------
# SORT
# Vai ordenar a sua lista de forma crescente
# ----------------------------------------------------------------------------------------------------------

lista = [2, 4, 67, 44, 3, 28, 23, 20, 37, 567]

lista.sort()

print(lista)
# [2, 3, 4, 20, 23, 28, 37, 44, 67, 567]

# Oredenar de forma decrescente

lista.sort(reverse=True)  # Ele vai ordenar de forma invertida

print(lista)
# [567, 67, 44, 37, 28, 23, 20, 4, 3, 2]


# ----------------------------------------------------------------------------------------------------------
# FUNCOES PARA LISTAS (ARRAY)
# ----------------------------------------------------------------------------------------------------------
# LEN
# Para saber o tamanho da lista,ou seja, quantos elementos tem na lista
# ----------------------------------------------------------------------------------------------------------

lista = [2, 4, 67, 44, 3, 28, 23, 20, 37, 567]

print(len(lista))  # 10

# SUM
# Vai somar todos os elementos da lista

lista = [2, 5, 3, 8]

somaDosElementos = sum(lista)

print('Soma de elemento: ', somaDosElementos)
# Soma de elemento:  18

print('A soma dos elementos da lista é : ', sum(lista))
# A soma dos elementos da lista é :  18


# ----------------------------------------------------------------------------------------------------------
# MAX
# Retorna o maior valor da lista
# ----------------------------------------------------------------------------------------------------------

lista = [2, 5, 1, 3, 8]

print('Maior elemento da lista: ', max(lista))
# Maior elemento da lista:  8


# ----------------------------------------------------------------------------------------------------------
# MIN
# Retorna o menor valor da lista
# ----------------------------------------------------------------------------------------------------------

print('Menor elemento da lista: ', min(lista))
# Menor elemento da lista:  1
