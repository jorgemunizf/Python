# SENTENÇAS DE ATRIBUIÇÃO

# ATRIBUIÇÃO SIMPLES

# x = 10
# Nessa atribuição, a variável x recebe o valor 10.

# ATRIBUIÇÃO MÚLTIPLA

# Python também permite a atribuição múltipla, ou seja, mais de uma variável
# receber atribuição na mesma linha.
# A título de exemplo, clique em Executar no emulador abaixo:

x, y = 2, 5
print(x)        # 2
print(y)        # 5

#============================================================================

# OPERADORES DE ATRIBUIÇÃO COMPOSTOS

# Executam operações matemáticas e atualizam o valor da variável utilizada.

# Ex.:

x = 10
x = x + 1
print(x)        # 11

# ou

y = 10
y += 1
print(y)        # 11



# Mais igual: +=

a = 10
a += 2
print('Mais igual:', a)     # 12

# -=

b = 10
b -= 2
print('Menos igual:', b)        # 8

# *=

c = 10
c *= 2
print('Vezes igual:', c)        # 20

# /=

d = 10
d /= 2
print('Dividido igual: ', d)        # 5.0

# %=

e = 10
e %= 3
print('Módulo igual: ', e)      # 1

#===========================================================================

# TROCA DE VARIÁVEIS

# Usando o metodo de ATRIBUIÇÃO MULTIPLA

# Exemplo:

a = 1
b = 2
# troca de variáveis usando variável auxiliar ‘temp’
temp = a
a = b
b = temp
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")

# troca de variáveis através de atribuição múltipla
a, b = b, a
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")

