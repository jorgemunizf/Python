# Faça um programa que calcule a média ponderada das notas de 3 provas

# A primeira e a segunda prova: peso 1
# A terceira prova: peso 2
# Ao final mostrar se a média do aluno e indicar se o aluno foi aprovado ou reprovado
# Nota para aprovação deve ser igual ou superior a 60 pontos.

notaProva1 = float(input('Digite a primeira nota: '))
notaProva2 = float(input('Digite a segunda nota: '))
notaProva3 = float(input('digite a terceira nota: '))

mediaPonderada = (notaProva1 * 1) + (notaProva2 * 1) + (notaProva3 * 2) / (1 + 1 + 3)

if mediaPonderada >= 60:
    print(f'Sua média foi de {mediaPonderada}, igual ou superior: APROVADO')
else:
    print(f'Sua média foi de {mediaPonderada}, menos de 60 pontos: REPROVADO')


