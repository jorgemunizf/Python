# TIPOS DE DADOS EM PYTHON

#=========================================================================

# NUMERICOS

# INTEIRO -> int

# Números inteiros, como na matemática - conjunto dos INTEIROS (Z)
# Podemos usar o underline para separar as casas decimais

x = 1_000_000

print(x)    # 1000000

# FLOAT (FLUTUANTE) -> float

# Números inteiros com parte decimal
# como na matemática - conjunto dos REAIS (R)

# a = 12.45
# a = 0.86

a = 50.0
print(type(a))  # <class "float">

# Número inteiro com numero intero o resultado é numero inteiro
# Número interro com numero float o resultado é numero float

print(type(2+3+1))      # <class 'int'>
print(type(2+3+1.0))    # <class 'float'>

print(2**3)             # 8
print(type(2**3))       # <class 'int'>
print(type(2.0**3))     # <class 'float'>

# No exemplo abaixo, o resultado é um número float

x = 5/2
print(x)    # 2.5

# Para resultar em um número inteiro usamos o operador //

b = 21 // 2
print(b)            # 10
print(type(b))      # <class 'int'>

# Para resultar na parte decimal usamos % ( resto da divisão )

c = 21 % 2
print(c)            # 1
print(type(c))      # <class 'int'>


#=========================================================================

# TIPO COMPLEXO

# Usado para manipular numeros complexos, usando a forma x + yj
# sendo X a parte real
# Y a parte imaginária do complexo

r = complex(2,5)

print(r)            # (2+5j)
print(type(r))      # <class 'complex'>

#=========================================================================
# TIPO BOOL ( BOLEANO )
# São expressões que podem ser avaliadas com um dos dois valores booleanos:
# True ou False.


n = 2 < 3
m = 2 > 3

print(n)      # True
print(m)      # False
