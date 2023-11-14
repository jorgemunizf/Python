# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
# aposentar. As condições para aposentadoria são
# - Ter pelo menos 65 anos,
# Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input('Digite sua idade: '))

if idade >= 65:
    print('Aposentadoria por idade')

tempo_contribuicao = int(input('Digite o tempo de contribuição: '))

if tempo_contribuicao >= 30:
    print('Aposentadoria por tempo de conribuição')
elif idade >= 60 and tempo_contribuicao >= 25:
    print('Aposentadoria por idade e tempo de contribuição')
else:
    print('Você ainda não tem os requisitos para se aposentar')
