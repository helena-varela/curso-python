# 8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
# função chamada show_magicians() que exiba o nome de cada mágico da lista.

magicos = ['joão','lucas','davi','fernando','carlos']

def show_magicians(magicos):
    """"Devolve o nome de cada mágico"""
    for magico in magicos:
        print(magico.title())

show_magicians(magicos)