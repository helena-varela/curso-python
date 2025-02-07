# 8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
# nome de uma cidade e seu país. A função deve exibir uma frase simples, como
# Reykjavik está localizada na Islândia. Forneça um valor default ao
# parâmetro que representa o país. Chame sua função para três cidades diferentes
# em que pelo menos uma delas não esteja no país default.

def describe_city(cidade, país = 'brasil'):
    """"descrevendo cidades"""
    print(cidade.title() + ' está localizada no ' + país.title() + '\n')
describe_city(cidade='natal')
describe_city(cidade='joão pessoa')
describe_city(cidade='california',país='EUA')