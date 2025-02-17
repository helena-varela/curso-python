# 9.10 – Importando Restaurant: Usando sua classe Restaurant mais recente,
# armazene-a em um módulo. Crie um arquivo separado que importe Restaurant.
# Crie uma instância de Restaurant e chame um de seus métodos para mostrar que
# a instrução import funciona de forma apropriada.

from Restaurante import Restaurant

restaurante1 = Restaurant('sicília','comida italiana')
restaurante1.describe_restaurant()
restaurante1.open_restaurante()