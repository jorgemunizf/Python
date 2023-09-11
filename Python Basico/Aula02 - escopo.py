# ESCOPO

# O escopo define em quais partes do programa uma variável é visível.
# Cada nome de variável em Python tem seu escopo e fora desse escopo
# o nome não existe, gerando um erro quando se tenta referenciar esse nome.
# Quanto ao escopo, chamamos as variáveis de globais ou locais.

# ============================================================================

# VARIAVEIS GLOBAIS
# Todos os nomes atribuídos no prompt interativo do Python,
# ou em um módulo fora de qualquer função são considerados como de escopo global

x = 10

print(x)


# "x" é uma variável global

# ============================================================================
# VARIÁVEL LOCAL

def multiplicador(numero):
    a = 2  # esta variável tem o escopo local
    print(f"Dentro da função , a variável vale: {a}")  # vale: 2
    return a * numero


a = 3  # esta variável tem o escopo glocal
b = multiplicador(5)
print(f"Fora da função, a variável vale: {a}")  # vale: 3


# Agora com uma pequena modificação

def multiplicador(numero):
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")    # Vale: 15


# Podemos alterar o valor da variável global dentro da função
# Usamos uma palavra reservada "global"

def multiplicador(numero):
    global a  # todas as referências à variável a são para a global
    a = 2  # a global será alterado
    print(f"Dentro da função,  variável  vale: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")



