# Leia um número fornecido pelo usuário. Se esse número for possitivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido

import math

numero = int(input("Digite um número para calcular a raiz quadrada: "))

if numero >= 0:
    raizQuadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raizQuadrada: .2f}")
else:
    print("O número digitado é inválido")
