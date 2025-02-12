# 8.14 – Carros: Escreva uma função que armazene informações sobre um carro em
# um dicionário. A função sempre deve receber o nome de um fabricante e um
# modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
# Chame a função com as informações necessárias e dois outros pares nome-valor,
# por exemplo, uma cor ou um opcional. Sua função deve ser apropriada para uma
# chamada como esta:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
# Mostre o dicionário devolvido para garantir que todas as informações foram
# armazenadas corretamente.

def car(nome_fabricante, modelo, **informações):
    """Armazena informações de um carro em um dicionário"""
    carro = {} #define um dicionario vazio
    carro['fabricante'] = nome_fabricante #dicionario[chave]=parametro 
    carro['modelo'] = modelo 
    for chave, valor in informações.items(): #definir chave-valor do argumento arbitrario
        carro[chave] = [valor]
    return carro #retorna o dicionario

carro = car('toyota','corolla', color = 'gray', year = 2020 )
print(carro)

