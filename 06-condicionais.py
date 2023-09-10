# ESTRUTURAS CONDICIONAIS

# ESTRUTURA CONDICIONAL: IF, ELIF e ELSE

"""
idade = int(input('Qual é a sua idade? '))

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
"""

"""
Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média
superior ou igual a 7, e "Reprovado(a)", caso a média seja inferior a 7.
"""

"""
media = float(input('Informe a sua média do estudante: '))

if media >= 7:
    print('PARABÉNS! Você foi Aprovado(a)!')
elif media >= 5:
    print('FALTA POUCO! Você está de recuperação')
else:
    print('INFELISMENTE você foi Reprovado(a)')]
"""

media = int(input('Informe a média do aluno: '))
presenca = int(input('Informe a presenca do aluno: '))

if media >= 7 and presenca >= 70:
    print('Aprovado(a)')
else:
    print('Reprovado(a)')
