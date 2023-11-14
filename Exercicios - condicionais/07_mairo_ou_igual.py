# Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais,
# imprima a mensagem "Números iguas"

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f"{num1} é maior que o {num2}")
elif num2 > num1:
    print(f"{num2} é maior que o {num1}")
else:
    print("Números iguas")
