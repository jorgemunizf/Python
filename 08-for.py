# LAÇO DE REPETIÇÃO: FOR

"""
 FOR -> pode declara qualquer no nome para a variavel
 RANGE -> Significa faixa, no exemplo abaixo a range(10) -> significa dentro da faixa tem numeros de 0 a 9
 ou seja, essa 'range' essa repetição aconteça 10x de (0 a 9)
 O range ele adimite até 3 parametros.
 Quando é informado somente 1 parametro, ele vai de 0 ate o numero do range - 1
 Quando é informado 2 parametros, range(1, 10), o primeiro parametro é de onde ele começa e vai até o 2 parametro - 1
 Quando é informado 3 parametros, range(0, 20, 2):
 - 1 param. -> De onde vai começar
 - 2 param. -> Até onde vai
 - 3 param. -> De quanto em quante ele vai pular (STEP)
 """


""" for variavel in range(10): # vai de 0 a 9
    print(variavel) """
''' for variavel in range(0, 20, 2):  # vai de 0 a 9
    print(variavel) '''

''' nota1 = float(input('Informe sua nota 1: '))
nota1 = float(input('Informe sua nota 2: '))
nota1 = float(input('Informe sua nota 3: ')) '''


# Usamos o F string para colocar a variável dentro do texto. f'texto de exemplo {variável}'

soma = 0

for i in range(1, 4):  # Começa no 1 e vai até o 3
    nota = float(input(f'Informe a sua nota {i}: '))

    soma += nota

media = soma / 3

print(media)



