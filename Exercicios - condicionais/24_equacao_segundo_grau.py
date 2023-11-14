# Calcule as raízes da equação de 2º grau.
# Lembrando que:

# x = -b±√▲ / 2a

# Onde

# ▲ = B²-4ac

# E ax² + bx + c = 0 representa uma equação de 2º grau.

# A variável "a" tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".
# • Se ▲ < 0, não existe real. Imprima a mensagem Não existe raiz.
# • Se ▲ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
# • Se ▲ >= 0, imprima as duas raízes reais.

import math

a = int(input('Digite o valor de "a" (deve ser diferente de zero): '))
b = int(input('Digite o valor de "b": '))
c = int(input('Digite o valor de "c": '))

if a == 0:
    print('Não é uma equação do segundo grau. O valor de "a" deve ser diferente de zero')
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('Não existe raiz real. ▲ é negativo')
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Raiz única: {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Raiz 1: {raiz1}')
        print(f'Raiz 2: {raiz2}')
