# Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
# Se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.

# • Equilátero - o triângulo que tem três lados iguais.
# • Isosceles - o triângulo que tem o comprimento de dois lados iguais.
# • Escaleno - o triângulo que tem os três lados diferentes.

ladoA = int(input('Digite o valor do lado A: '))
ladoB = int(input('Digite o valor do lado B: '))
ladoC = int(input('Digite o valor do lado C: '))

if ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
    print('Os valores de A, B, C formam o: Triangulo Escaleno')
elif ladoA == ladoB != ladoC or ladoB == ladoC != ladoA or ladoA == ladoC != ladoB:
    print('Os valores de A, B, C formam o: Triangulo Equilatero')
elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
    print('Os valores de A, B, C formam o: Triangulo Isosceles')
