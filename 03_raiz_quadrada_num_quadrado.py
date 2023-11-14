# Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário imprima o número ao quadrado

numero = int(input('Digite um número: '))

if numero > 0:
    raizQuadrada = numero ** 0.5
    print(f'A raiz quadrado do número {numero} é {raizQuadrada}')
else:
    numeroQuadrado = numero ** 2
    print(f'O quadrado do número {numero} é {numeroQuadrado}')
        
