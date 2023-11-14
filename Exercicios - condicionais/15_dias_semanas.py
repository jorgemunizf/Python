# Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
# da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e
# assim por diante.
def obterDiaDaSemana(numero):
    dias = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }

    return dias.get(numero, 'Número inválido. Deve estar entre 1 e 7')


numero = int(input('Digite um número entre 1 e 7 para saber o dia da semana: '))
resultado = obterDiaDaSemana(numero)
print(resultado)
