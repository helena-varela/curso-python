# 9.13 – Reescrevendo o programa com OrderedDict: Comece com o Exercício
# 6.4 (página 155), em que usamos um dicionário-padrão para representar um
# glossário. Reescreva o programa usando a classe OrderedDict e certifique-se de
# que a ordem da saída coincida com a ordem em que os pares chave-valor foram
# adicionados ao dicionário.
from collections import OrderedDict

glossário = OrderedDict

glossário = {'tupla': 'estrutura de dados que armazena um conjunto de valores imutáveis',
             'pop':'deve ser utilizado para remover um elemento com um índice específico',
             'elif': 'abreviação de "else if" e permite verificar múltiplas condições sequencialmente',
             'string': 'usado para armazenar mensagens de texto',
             'str':'transforma números em strings',
             'sorted': 'coloca em ordem alfabética',
             'range': 'retorna uma sequência de números',
             'len':'retorna o número de objetos',
             'del': 'deleta itens',
             'append': 'adiciona um item ao final da lista',
             }

for palavra, significado in glossário.items():
    print(palavra.title() + ': ' + significado.title() + '.\n')