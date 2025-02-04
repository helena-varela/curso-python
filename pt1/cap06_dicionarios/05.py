#6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
#cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
#• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
#pelo Egito.
#• Use um laço para exibir o nome de cada rio incluído no dicionário.
#• Use um laço para exibir o nome de cada país incluído no dicionário

rios = {'nilo':'egito',
        'amazonas': 'brasil',
        'mississippi':'eua',
        }

for rio, país in rios.items():
    print('o rio ' + rio.title() + ' corre pelo ' + país.title() + '.')

print('\n')

for rio, país in rios.items():
    print(rio.title())

print('\n')

for rio, país in rios.items():
    print(país.title())