# Faça um programa que receba a altura e o sexo de uma pessoa
# Calcule e mostre o peso ideal
# Formula utilizada:

# h - corresponde à altura

# Homen: (72.7 * h) - 58
# Mulher: (62.1 * h) - 44.7

sexo = str(input('Diga qual o seu sexo "Maculino ou Feminino": '))

if sexo == "Masculino":
    alturaHomen = float(input('Digite sua altura: '))

    pesoIdeal = (72.7 * alturaHomen) - 58
    print(f'O peso ideal para a altura de {alturaHomen} é de {pesoIdeal}')
else:
    alturaMulher = float(input('Digite sua altura: '))

    pesoIdeal = (62.1 * alturaMulher) - 44.7
    print(f'O peso ideal para a altura de {alturaMulher} é de {pesoIdeal: .2f}')
