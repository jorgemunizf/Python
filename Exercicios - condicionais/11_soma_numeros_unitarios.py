# Escreva um programa que leia um número inteiro maior que zero
# Soma todos os seus algarismos
# Se o número for não for maior que zero imprimir a menasgem: "Número inválido"

numero = int(input('Digite um número inteiro maior que zero: '))

if numero > 0:
    somaDigitos = sum(int(digito) for digito in str(numero))
    print(f'A soma dos algarismos do número {numero} é: {somaDigitos}')
else:
    print("Número inválido")

