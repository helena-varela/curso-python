#6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
#cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
#cada cidade e inclua o país em que a cidade está localizada, a população
#aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
#devem ser algo como country, population e fact. Apresente o nome de cada
#cidade e todas as informações que você armazenou sobre ela.

cities = {
    'natal': {
        'country':'brasil',
        'population': 100,
        'fact': 'é a cidade do sol',
    },
    'tokyo': {
        'country': 'japão',
        'population': 200,
        'fact':'famoso por ser muito tecnológico',
    },
    'california': {
        'country':'eua',
        'population': 300,
        'fact': 'é o terceiro maior estado dos EUA'
    }
}

for cidade, info in cities.items():
    print(cidade.title() + ':\n' + '-País: ' + str(info['country'].title()))
    print('-Populção: ' + str(info['population']))
    print('-Fato: ' + str(info['fact']).title() + '\n')