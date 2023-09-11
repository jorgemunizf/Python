# FORMATAÇÃO DE DADOS DE SAÍDA


# Quando desejamos que a saída siga determinado padrão – por exemplo,
# de hora ou de data – existem algumas possibilidades para usar a função print().
# É sempre possível utilizar a concatenação de strings, com o operador +,
# para montar a frase como quisermos.
# Suponha que tenhamos as seguintes variáveis:

hora = 10
minutos = 26
segundos = 18

# Chamamos a função print() com o separador : (dois pontos) da seguinte forma:


print(str(hora) + ':' + str(minutos) + ':' + str(segundos))
# retorna -> 10:26:18

#----------------------------------------------------------------------------

# Porém, existe outra forma, usando o FORMAT().


print('{} : {} : {}'.format(hora, minutos, segundos))
# retorna -> 10 : 26 : 18

#----------------------------------------------------------------------------

# Para tornar a saída formatada ainda mais intuitiva,
# basta utilizar a letra ‘f’ no início dos parâmetros da função print()
# e colocar cada variável dentro das chaves na posição em que deve
# ser impressa.


print(f'{hora}:{minutos}:{segundos}')
# retorna -> 10:26:18


#----------------------------------------------------------------------------

# Também é possível especificar a largura de campo para exibir um inteiro.
# Se a largura não for especificada, ela será determinada pela quantidade
# de dígitos do valor a ser impresso.


print('{:4},{:5}'.format(10, 100))
# retorna -> __10,__100


# Observe que os valores 10 e 100 foram impressos com espaços em branco à esquerda.
# Isso ocorreu porque definimos que a primeira variável deveria ser
# impressa com 4 espaços com {:4} (2 foram ocupados e 2 ficaram em branco),
# e que a segunda variável deveria ser impressa com 5 espaços com {:5}
# (3 foram ocupados e 2 ficaram em branco).


#----------------------------------------------------------------------------

# Pode imprimir valores de ponto flutuante com a precisão definida.

print('{:8.5}'.format(10 / 3))
# retorna -> __3.3333

# Ao usar {:8.5}, estamos determinando que a impressão será com 8 espaços,
# mas apenas 5 serão utilizados.

# ===========================================================================

# IMPRESSÃO DE SEQUÊNCIA

# Em Python, basta chamar a função print() passando como parâmetro a sequência

seq = [0, 1, 2]
print(seq)

# retorna -> [0, 1, 2]

#----------------------------------------------------------------------------

# Para imprimir uma substring, por exemplo, basta utilizar os colchetes
# para indicar o intervalo de índices que deve ser impresso

str = 'Hello World'
print(str[0:4])

# retorno -> Hell

print(str[2:8])

# retorna -> llo Wo

#----------------------------------------------------------------------------

# Também é possível imprimir a string como lida da direita para a esquerda.
# Para isso, deve-se utilizar [: : -1]. Esse valor -1 indica que a
# leitura dos caracteres será feita no sentido oposto ao tradicional

print(str[::-1])
# retorno -> dlroW olleH

print(str[8:2:-1])
# retorno -> roW ol

