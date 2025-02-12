# 8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
# Chame a função make_great() com uma cópia da lista de nomes de mágicos.
# Como a lista original não será alterada, devolva a nova lista e armazene-a em uma
# lista separada. Chame show_magicians() com cada lista para mostrar que você
# tem uma lista de nomes originais e uma lista com a expressão o Grande
# adicionada ao nome de cada mágico.

magicos = ['joão','lucas','davi','fernando','carlos']

def show_magicians(magicos):
    """"Devolve o nome de cada mágico"""
    for magico in magicos:
        print(magico.title())

def make_great(magicos):
    """"Adiciona a expressão 'o grande' ao nome."""
    indice = 0 #variável que contém o valor 0
    while indice < len(magicos): #enquanto o valor da variável for menor que os elementos de magicos
        magicos[indice] += ', O Grande' #adiciona ', O Grande' a cada mágico, a variável 'indice' indica o indice da lista
        indice += 1 #ao final é somado 1 a variável 'indice'

print('\nNomes originais de make_great:')
Original = make_great(magicos[:])

print('Nomes originais de show_magicians:')
show_magicians(magicos[:])