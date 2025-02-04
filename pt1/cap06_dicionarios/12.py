#6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o
#bastante para poderem ser estendidos de várias maneiras. Use um dos programas
#de exemplo deste capítulo e estenda-o acrescentando novas chaves e valores,
#alterando o contexto do programa ou melhorando a formatação da saída.

cities = {
    'natal': {
        'country':'brasil',
        'population': 100,
        'fact': 'é a cidade do sol',
        'age' : 1300
    },
    'tokyo': {
        'country': 'japao',
        'population': 200,
        'fact':'famoso por ser muito tecnológico',
        'age':1400
    },
    'california': {
        'country':'eua',
        'population': 300,
        'fact': 'é o terceiro maior estado dos EUA',
        'age': 1000,
    }
}

for cidade, info in cities.items():
    print(cidade.title() + ":")
    print("-País: " + info['country'][0].upper() + info['country'][1:])
    print("-População: " + str(info['population']))
    print("-Fato: " + info['fact'][0].upper() + info['fact'][1:])
    print("-Ano: " + str(info['age']) + "\n")
