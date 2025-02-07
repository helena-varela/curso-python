# 8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
# camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
# uma camiseta grande e outra média com a mensagem default, e uma camiseta de
# qualquer tamanho com uma mensagem diferente.

def make_shirt(tamanho='grande', texto='Eu amo Python'):
    """"Fazendo camisetas"""
    print('O tamanho da camiseta será ' + tamanho + ' e terá estampado ' + texto + '\n')
make_shirt()
make_shirt(tamanho='médio')
make_shirt(tamanho='PP',texto='Party Anthem')