#6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
#dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
#tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
#chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer
#isso, apresente tudo que você sabe sobre cada animal de estimação.

lulu = {'especie':'cachorro',
        'dono': 'julia',
        }

spot = {'especie':'cachorro',
          'dono': 'joao',
          }

cenoura = {'especie':'coelho',
           'dono': 'maria',
           } 

pets = [lulu, spot, cenoura]

for pet in pets:
    print('Espécie: ' + str(pet['especie']).title()) 
    print('Dono: ' + str(pet['dono']).title() + '\n')