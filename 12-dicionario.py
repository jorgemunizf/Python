# DICIONÁRIOS


# ----------------------------------------------------------------------------------------------------------
# CRIANDO DICIONÁRIOS
# ----------------------------------------------------------------------------------------------------------

dicionario = {}  # Cria um dicionário abrindo e fechando chaves
dicionario = dict()  # Função para criar um dicionário

# O dicionário pode conter: number, string, bool, ...
dicionario = {'nome': 'Bruno', 'idade': 32, 'altura': 1.73}

print(dicionario)
# {'nome': 'Bruno', 'idade': 32, 'altura': 1.73}

print(dicionario['altura'])
# 1.73


# ----------------------------------------------------------------------------------------------------------
# ADICIONANDO ELEMENTOS EM UM DICIONÁRIO
# ----------------------------------------------------------------------------------------------------------

dicionario['Programador'] = True

print(dicionario)
# {'nome': 'Bruno', 'idade': 32, 'altura': 1.73, 'Programador': True}


# Caso vc coloque uma chave com um valor a uma chave que já existe, ele vai sobrescrever
dicionario['altura'] = 1.85

print(dicionario)
# {'nome': 'Bruno', 'idade': 32, 'altura': 1.85, 'Programador': True} -> A altura foi alterada de 1.73 para 1.85


# ----------------------------------------------------------------------------------------------------------
# ITERANDO SOBRE UM DICIONÁRIO
# ----------------------------------------------------------------------------------------------------------

for chave in dicionario:
    print(chave)
# Ele vai percorrer as chaves: nome idade altura Programador

for chave in dicionario:
    print(chave, dicionario[chave])
# Vai imprimir tanto a chave quanto o seu valor
#     nome    Bruno
#     idade   32
#     altura  1.85
#     Programador  True


# ----------------------------------------------------------------------------------------------------------
# TESTANDO A EXISTÊNCIA DE UMA CHAVE
# ----------------------------------------------------------------------------------------------------------
# Caso queira saber se existe uma chave dentro do cicionário

print('peson' in dicionario)
# False

print('altura' in dicionario)
# True


