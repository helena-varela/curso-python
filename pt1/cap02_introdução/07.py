# 2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
# pessoa e inclua alguns caracteres em branco no início e no final do nome. 
# Lembrese de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
# Exiba o nome uma vez, de modo que os espaços em branco em torno do nome
# sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções de
# remoção de espaços: lstrip(), rstrip() e strip().

nome = '         joao   '
print('\t' + nome)
print(nome.strip() + '\n')
print(nome.lstrip() + '\n')
print(nome.rstrip())