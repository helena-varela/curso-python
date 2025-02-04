# 3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
# Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
# informando o número de pessoas que você está convidando para o jantar.
lista = ['neto','joao','tereza','jonas','ju','vivi']
print(len(lista))
mensagem = 'oii nao vai dar :( a mesa nao chegou a tempo, '

desconvidado = lista.pop()
print(mensagem + desconvidado)

desconvidado = lista.pop()
print(mensagem + desconvidado)

desconvidado = lista.pop()
print(mensagem + desconvidado)

desconvidado = lista.pop()
print(mensagem + desconvidado)

mensagem_1 = 'oii vc ainda pode vir, '
print(mensagem_1 + str(lista[0]))
print(mensagem_1 + str(lista[1]))

del lista[0]
del lista[0]
print(lista)
print(len(lista))
