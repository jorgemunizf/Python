# Determine se um determinado ano lido é bissexto.
# Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
# Por exemplo: 1988, 1992, 1996

ano = int(input('Digite o ano para saber se é bissexto: '))

if ano % 400 == 0 or ano % 4 == 0 or ano % 100 == 1:
    print(f'O ano {ano} é um ano bissexto')
else:
    print(f'O ano {ano} não é um ano bissexto')
