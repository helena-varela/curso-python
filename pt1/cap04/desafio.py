#qnd eu cheguei no lab tava sem o arenito
pedras = ['quartzo', 'feldspato', 'arenito', 'granito', 'xisto'] 
print('pedra 1 é ' + pedras[0])
print('pedra 2 é ' + pedras[1])
print('pedra 3 é ' + pedras[2])
print('pedra 4 é ' + pedras[3])
print('pedra 5 é ' + pedras[4])
#a mesa dps que cheguei do lanche
pedras[2] = "mármore"
print('pedra 1 é ' + pedras[0])
print('pedra 2 é ' + pedras[1])
print('pedra 3 é ' + pedras[2])
print('pedra 4 é ' + pedras[3])
print('pedra 5 é ' + pedras[4])

print('um novo dia')
pedras.append("magnetita")
print(pedras)

print("laurao chegou")
pedras.insert(1, 'basalto')
pedras.insert(5, 'basalto')
print(pedras)

# Remover
# del
# .pop()

del pedras[0]
del pedras[-1]

print("\n\n Antes de remover cada pedra")
print(pedras)
del pedras[0]

del pedras[0]

del pedras[0]

del pedras[0]

del pedras[0]

del pedras[0]

print("Depoois de remover cada pedra")
print(pedras)


comidas = ['banana', 'maça', 'pera']
print("Comidas que temos:")
print("\t" + str(comidas))

acabei_de_comer = comidas.pop(0)
print(comidas)

acabei_de_comer = comidas.pop()
print(comidas)
