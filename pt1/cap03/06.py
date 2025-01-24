#3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
#portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.
#• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
#uma instrução print no final de seu programa informando às pessoas que você
#encontrou uma mesa de jantar maior.
#• Utilize insert() para adicionar um novo convidado no início de sua lista.
#• Utilize insert() para adicionar um novo convidado no meio de sua lista.
#• Utilize append() para adicionar um novo convidado no final de sua lista.
#• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.
lista = ['joao', 'lila','ju']
print('os convidados serão' + str(lista))

nao_vai = lista.pop(1)
print(nao_vai + ' nao vai comparecer')

lista.insert(1, 'jonas')
print('a nova lista sera ' + str(lista))

convite = "oii vem jantar cmg "
print(convite + lista[0])
print(convite + lista[1])
print(convite + lista[2])

lista = ['joao', 'jonas','ju']
lista.insert(0, 'neto')
lista.insert(2, 'tereza')
lista.append('vivi')
print('agora a lista é ' + str(lista))

convite = 'oii achei uma mesa maior vms todos, '
print(convite + lista[0])
print(convite + lista[1])
print(convite + lista[2])
print(convite + lista[3])
print(convite + lista[4])
print(convite + lista[5])
