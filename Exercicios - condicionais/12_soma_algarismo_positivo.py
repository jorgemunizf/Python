# Faça um programa que leia um numero inteiro
# Se for negativo: imprimir "Número inválido"
# Se for positivo: somar os algarismos

numero = int(input('Digite um número inteiro: '))

if numero < 0:
    print("Número inválido")
else:
    algarismo = sum(map(int, str(numero)))
    print(f'O algarismo do número {numero} é: {algarismo}')


