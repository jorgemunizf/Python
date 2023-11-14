# Escreva um programa que, dado dois números inteiros, mostre na tela o maior deles, assim como a diferença
# existente entre ambos

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f"{num1} é maior que o {num2}")
    print(f'A diferença entre os números {num1} e número {num2} é {num1 - num2}')
else:
    print(f"{num2} é maior que o {num1}")
    print(f'A diferença entre os números {num2} e número {num1} é {num2 - num1}')
