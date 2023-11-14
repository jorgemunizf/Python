# Uma empresa vende o mesmo produto para quatro diferentes estados.
# Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
# Faça um programa em que o usuário entre com o valor e o estado destino do produto
# E o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido.
# Se o estado digitado não for válido, mostrar uma mensagem de erro.

valorProduto = float(input('Digite o valor do produto para calcular o valor do imposto: '))

print('Escolha o estado para calcular o imposto sobre o produto:')
print('1 - MG')
print('2 - SP')
print('3 - RJ')
print('4 - MS')

estado = input('Digite um número para operação desejada: ')

if estado.isdigit():
    estado = int(estado)

    if estado < 1 or estado > 4:
        print('Opção inválida. Programa encerrado.')
    else:
        if estado == 1:
            valorProdutoImposto = (valorProduto * 0.07) + valorProduto
            print(f'O valor do produto no estado de MG é: {valorProdutoImposto}')
        elif estado == 2:
            valorProdutoImposto = (valorProduto * 0.12) + valorProduto
            print(f'O valor do produto no estado de SP é: {valorProdutoImposto}')
        elif estado == 3:
            valorProdutoImposto = (valorProduto * 0.15) + valorProduto
            print(f'O valor do produto no estado de RJ é: {valorProdutoImposto}')
        elif estado == 4:
            valorProdutoImposto = (valorProduto * 0.08) + valorProduto
            print(f'O valor do produto no estado de MS é: {valorProdutoImposto}')
