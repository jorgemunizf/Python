#   OPERADORES NUMERICOS

#============================================================================

# + - SOMA

soma = 2.5 + 1.3
print("A soma é:", soma)
# 3.8

# - - SUBTRAÇÃO

sub = 2.5 - 1.3
print("A subtração é:", sub)
# 1.2

# * - MULTIPLICAÇÃO

multip = 2.5 * 1.3
print("A multiplicação é:", multip)
# 3.25

# / - DIVISÃO

div = 2.5 / 1.3
print("A divisão é:", div)
# 1.923076923076923

# // - DIVISÃO INTEIRA

divInt = 9 // 2
print("A divisão inteira é:", divInt)
# 4

# % - RESTO DA DIVISÃO

restDiv = 9 % 2
print("O resto da divisão é:", restDiv)
# 1

# abs - VALOR ABSOLUTO

valorAbs = abs(-2.5)
print("O valor absoluto é:", valorAbs)
# 2.5

# ** - EXPONENCIAÇÃO (POTÊNCIA)

exp = 2 ** 4
print("A potência é:", exp)
# 16

#============================================================================

# OPERADORES DE COMPARAÇÃO

# O resultado são valores booleanos ( True ou False )

# < - Menor que

print("Menor que:", (2 < 3))        # True
print("Menor que:", (3 < 2))        # False

# <= - Menor ou igual a

print("Menor ou igual:", (2 <= 2))       # True
print("Menor ou igual:", (2 <= 3))       # True
print("Menor ou igual:", (3 <= 2))       # False

# > - Maior que

print("Maior que:", (2 > 3))       # False
print("Maior que:", (3 > 2))       # True

# >= - Maior ou igual a

print("Maior ou igual:", (2 >= 2))       # True
print("Maior ou igual:", (2 >= 3))       # False
print("Maior ou igual:", (3 >= 2))       # True

# == - Igual

print("Igual:", (2 == 3))       # False
print("Igual:", (2 == 2))       # True

# != - Não é igual

print("Não é igual:", (2 != 3))       # True
print("Não é igual:", (2 != 2))       # False

#============================================================================

# OPERADORES BOOLEANOS

# O resultado são valores booleanos ( True ou False )

# AND ( e )

# Verdadeiro se todos forem verdadeiros.
# Falso se todos forem falso

print("AND:", (2 < 3 and 4 > 2))      # True
print("AND:", (2 > 3 and 4 < 2))      # False

# OR ( ou )

# Verdadeiro se um ou todos for Verdadeiro
# Falso se todos forem falso

print("OR:", (2 < 3 or 4 > 2))      # True
print("OR:", (2 < 3 or 4 < 2))      # True
print("OR:", (2 > 3 or 4 < 2))      # False

# NOT ( não )

# Verdadeiro é Falso
# Falso é Verdadeiro
