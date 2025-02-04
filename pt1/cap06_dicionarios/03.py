#6.3 – Glossário: Um dicionário Python pode ser usado para modelar um dicionário
#de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
#• Pense em cinco palavras relacionadas à programação que você conheceu nos
#capítulos anteriores. Use essas palavras como chaves em seu glossário e
#armazene seus significados como valores.
#• Mostre cada palavra e seu significado em uma saída formatada de modo
#elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
#significado, ou apresentar a palavra em uma linha e então exibir seu significado
#indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
#para inserir uma linha em branco entre cada par palavra-significado em sua saída.

glossário = {'tupla': 'estrutura de dados que armazena um conjunto de valores imutáveis',
             'pop':'deve ser utilizado para remover um elemento com um índice específico',
             'elif': 'abreviação de "else if" e permite verificar múltiplas condições sequencialmente',
             'string': 'usado para armazenar mensagens de texto',
             'str':'transforma números em strings',
             }

print('Tupla:\n\t' + glossário['tupla'].title())
print('Pop:\n\t' + glossário['pop'].title())
print('Elif:\n\t' + glossário['elif'].title())
print('String:\n\t' + glossário['string'].title())
print('Str:\n\t' + glossário['str'].title())