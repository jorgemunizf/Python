# FUNCOES (DEF)

# def "nome da função"(parâmetro):
# ......... identação de 4 espaços

# 1. O que são funções e por que são utilizadas?

# Usado para quando vc quer usar um bloco de código complexo (uma lógica) repetidas vezes sem
# precisar ficar repetindo o bloco de código

# Funções utilizadas anteriormente:

# print() - Imprimir uma mensagem (int, float, str) no console (terminal, cmd)
# input() - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
# len() - Recebe uma lista e retorna o tamanho dela
# max()   - Retorna o maior valor de uma lista

##############################################################################################
# 2. CRIAÇÃO DE FUNÇÃO
##############################################################################################
##############################################################################################
# FUNÇÃO INICIAL
##############################################################################################
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')


saudacao()


# Seja bem-vindo(a)!
# Olá, é um prazer ter você fazendo parte desse curso!

##############################################################################################
# FUNÇÃO COM PARÂMETROS
##############################################################################################
def saudacao(nome, curso):  # A função está recebendo os parâmetros "nome" e "curso"
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')


saudacao('Jorge', 'Python')
saudacao("Aline", "Javascript")


# Seja bem-vindo(a), Jorge!
# Olá, é um prazer ter você fazendo parte do curso de Python!
# Seja bem-vindo(a), Aline!
# Olá, é um prazer ter você fazendo parte do curso de Javascript!

##############################################################################################
# FUNÇÃO COM PARÂMETRO DEFAULT
##############################################################################################
def saudacao(nome,
             curso='Python'):  # A função está recebendo um parâmetro default "curso = 'Python', ou seja, está colocando valor no parâmetro
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')


saudacao('Jorge')  # Por padrão o nome do curso já é colocado dentro do texto


# Seja bem-vindo(a), Jorge!
# Olá, é um prazer ter você fazendo parte do curso de Python!

##############################################################################################
# FUNÇÃO COM RETORNO
##############################################################################################

def soma(num1, num2):
    return num1 + num2  # Quando colca o retorno a função para de executar, só usar quando finalizar a função


resultado = soma(4, 6)

print('O resultado da soma é', resultado)


# O resultado da soma é 10


def calculadora(num1, num2, operacao='+'):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2

calculadora(10, 20)

print(calculadora(10,20, '*'))
# 200


