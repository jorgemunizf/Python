# Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
# Se a prestação for maior que 20% do salário imprima: "Empréstimo não concedido"
# Caso contrário imprima: "Empréstimo concedido

salario = float(input('Digite o valor do salário: '))
parcelaEmprestimo = float(input('Digite o valor da parcela do empréstimo: '))

limiteMarge = salario * 0.2

if parcelaEmprestimo > limiteMarge:
    print("empréstimo não concedido")
else:
    print("Empréstimo concedido")

