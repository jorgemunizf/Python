# Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# - O número digitado ao quadrado;
# - A raiz quadrada do número digitado;

numero = int(input('Digite um número: '))

if numero > 0:
    numQuadrado = numero ** 2
    raziQuadrada = numero ** 0.5
    print(f'O quadrado do número {numero} é {numQuadrado}')
    print(f'A raiz quadrada do número {numero} é {raziQuadrada}')
else:
    print('Por favor digite um número positivo')
