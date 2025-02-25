# 10.8 – Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo
# menos três nomes de gatos no primeiro arquivo e três nomes de cachorro no
# segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o
# conteúdo do arquivo na tela. Coloque seu código em um bloco try-except para
# capturar o erro FileNotFound e apresente uma mensagem simpática caso o
# arquivo não esteja presente. Mova um dos arquivos para um local diferente de seu
# sistema e garanta que o código no bloco except seja executado de forma
# apropriada.

try:
    with open('dogs.txt') as object:     
        arquivo = object.read()

    with open('cats.txt') as object:  
        arquivo2 = object.read()

except FileNotFoundError:
    print('File não encontrada')

else: print('Cachorros:\n' + arquivo.title() + '\n') 
print('Gatos:\n' + arquivo2.title() + '\n')