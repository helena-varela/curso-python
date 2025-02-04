#6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com um
#laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de
#instruções print por um laço que percorra as chaves e os valores do dicionário.
#Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de
#Python ao seu glossário. Ao executar seu programa novamente, essas palavras e
#significados novos deverão ser automaticamente incluídos na saída.

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
 