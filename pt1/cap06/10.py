#6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
#147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
#apresente o nome de cada pessoa, juntamente com seus números favoritos.

numeros_favoritos = {'fulano': [20, 24], 
                     'ciclano': [13, 15, 17],
                     'beltrano': [10, 45, 78],
                     'maria': [22, 71], 
                     'juliana': [6, 2006],
                     }

for nomes, numeros in numeros_favoritos.items():
    print(nomes.title() + '\n -' + str(numeros))