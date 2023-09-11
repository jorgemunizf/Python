# ENTRADA DE DADOS - INPUT()

# Ela tanto exibe na tela o pedido, como permite que o valor informado
# pelo usuário seja armazenado em uma variável do seu programa.

# A função input() trata tudo o que for digitado pelo usuário como uma string

# Ex.:

# nome = input('Entre com seu nome: ')
# print(nome)
#
# numero = input('Entre com um inteiro: ')
# print(type(numero))     # retorna <class 'str'>


#============================================================================

# FUNÇÃO EVAL()

# Recebe uma string, mas trata como um valor numérico.

s = '1 + 2'
print(type(s))      # <class 'str'>
print(eval(s))      # 3


numero = eval(input('Entre com um inteiro: '))
numero = numero + 2
print(numero)       # retorna 6


