# Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou
# 5, mas não simultaneamente pelos dois.

numero = int(input('Digite um número para saber se é divisível por 3 ou 5: '))

if numero % 3 == 0 and numero % 5 == 0:
    print(f'O número {numero} é divisivel por 3 e 5')
elif numero % 3 == 0:
    print(f'O número {numero} é divisivel por 3')
elif numero % 5 == 0:
    print(f'O número {numero} é divisivel por 5')
else:
    print('O número digitado não e divisível por 3 ou 5')
