# Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
# A = (basemaior + basemenor) * altura / 2
# Lembre-se a base maior e a base menor devem ser números maiores que zero.

baseMaior = int(input('Digite o valor da base maior do trapezio: '))
baseMenor = int(input('Digite o valor da base menor do trapezio: '))

if baseMaior < 0 or baseMenor < 0:
    print('O valor da base maior e base menor tem que ser maio que 0')
else:
    areaTrapezio = (baseMaior + baseMenor) / 2
    print(f'A área do trapezio é: {areaTrapezio}')
