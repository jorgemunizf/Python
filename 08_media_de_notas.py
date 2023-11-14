# Faça um programa que leia 2 notas de um aluno exiba a média das notas
# Verifique se as notas são válidas(0 a 10)
# Caso não tenha uma nota válida imprima uma mensagem informando

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f"A média das notas {nota1} e {nota2} é {media}")
else:
    print('Nota inválida')
