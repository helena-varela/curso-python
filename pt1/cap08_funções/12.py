# 8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
# pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos
# itens quantos forem fornecidos pela chamada da função e deve apresentar um
# resumo do sanduíche pedido. Chame a função três vezes usando um número
# diferente de argumentos a cada vez.

def pedido_sanduiche(*ingredientes):
    """aceita uma lista de ingredientes"""
    for ingrediente in ingredientes:
        print('-' + ingrediente.title())

pedido_sanduiche('carne')
pedido_sanduiche('queijo', 'tomate')
pedido_sanduiche('cebola','frango','cebola')