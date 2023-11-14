# Faça um programa que mostre ao usuário um menu com 4 opções de operações ma-
# temáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu pro-
# grama então pede dois valores numéricos e realiza a operação, mostrando o resultado e
# saindo.


print('Escolha a operação:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

escolha = input('Digite um número para operação desejada: ')

if escolha.isdigit():
    escolha = int(escolha)

    if escolha < 1 or escolha > 4:
        print('Opção inválida. Programa encerrado.')
    else:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if escolha == 1:
            resultado = num1 + num2
            # print(f'A soma é: {resultado}')
            print('O resultado da soma é: ', resultado)
        elif escolha == 2:
            resiltado = num1 - num2
            print(f'A subtração é: {resiltado}')
        elif escolha == 3:
            resiltado = num1 * num2
            print(f'A multiplicação é: {resiltado}')
        elif escolha == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"A divisão é: {resultado}")
            else:
                print("Não é possível dividir por zero. Programa encerrado.")

else:
    print('Entrada inválida. Digite um número inteiro. Programa encerrado')
