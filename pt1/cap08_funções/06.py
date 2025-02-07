# 8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
# aceite o nome de uma cidade e seu país. A função deve devolver uma string
# formatada assim:
# "Santiago, Chile"
# Chame sua função com pelo menos três pares cidade-país e apresente o valor devolvido.

def city_country(cidade, país):
    """"devolve a cidade e o país"""
    string = cidade.title() + ', ' + país.title()
    return string

cidades = city_country('natal', 'brasil')
print(cidades)
cidades = city_country('barcelona', 'espanha')
print(cidades)
cidades = city_country('tokyo','japão')
print(cidades)