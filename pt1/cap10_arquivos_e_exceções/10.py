# 10.10 – Palavras comuns: Acesse o Projeto Gutenberg (http://gutenberg.org/ ) e
# encontre alguns textos que você gostaria de analisar. Faça download dos arquivostexto dessas obras ou copie o texto puro de seu navegador para um arquivo-texto
# em seu computador.
# Você pode usar o método count() para descobrir quantas vezes uma palavra ou
# expressão aparece em uma string. Por exemplo, o código a seguir conta quantas
# vezes a palavra 'row' aparece em uma string:

alice = r'C:\Users\lelena\Documents\curso-python\pt1\cap10_arquivos_e_exceções\alice.txt'

with open(alice) as object:
    conteudo = object.read()

word = object.split()
num = len(word)
print(num)