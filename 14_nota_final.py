# A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
# respectivamente
# - Um trabalho de laboratório
# - Uma avaliação semestral
# - Um exame final

# A média das três notas mencionadas anteriormente abedece aos pesos:

# Trabalho de Laboratório: 2
# Avaliação Semestral: 3
# Exame Final: 5

# Mostre na tela se o aluno esta:

# Aprovado: 5
# Recuperação: 3 a 4,9
# Reprovado: 0 a 2,9

notaTrabalhoLaboratorio = float(input('Digite a nota do Trabalho de Laboratório: '))
notaAvaliacaoSemestral = float(input('Digite a nota da Avaliação Semestral: '))
notaExameFinal = float(input('Digite a nota do Exame Final: '))

# media = (notaTrabalhoLaboratorio * 2) + (notaAvaliacaoSemestral * 3) + (notaExameFinal * 5) / 2 + 3 + 5
media = (notaTrabalhoLaboratorio + notaAvaliacaoSemestral + notaExameFinal) / 3

if media >= 5:
    print(f'Sua média foi de {media: .2f}: APROVADO')
elif 3 < media < 4.9:
    print(f'Sua média foi de {media: .2f}: RECUPERAÇÃO')
elif 0 < media < 2.9:
    print(f'Sua média foi de {media: .2f}: REPROVADO')
