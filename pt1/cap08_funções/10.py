# 8.10 – Grandes mágicos: Comece com uma cópia de seu programa do Exercício
# 8.9. Escreva uma função chamada make_great() que modifique a lista de
# mágicos acrescentando a expressão o Grande ao nome de cada mágico. Chame
# show_magicians() para ver se a lista foi realmente modificada.

def show_magicians(magicos):
    """"Devolve o nome de cada mágico"""
    for magico in magicos:
        print(magico.title())

def make_great(magicos):
    """"Adiciona a expressão 'o grande' ao nome."""
    indice = 0
    while indice < len(magicos):
        magicos[indice] += ", o grande" # magicos[indice] = magicos[indice] + ",  o grande"
        indice += 1 # indice = indice + 1

    # Pode se fazer assim:
    # for indice in range(0, len(magicos)):
    #     magicos[indice] = magicos[indice] + " o grande!"

magicos = ['joão','lucas','davi','fernando','carlos']

print('Antes da modificação:')
show_magicians(magicos)

print('\nDepois da modificação:')
make_great(magicos)
show_magicians(magicos)