# 10.1 – Aprendendo Python: Abra um arquivo em branco em seu editor de texto e
# escreva algumas linhas que sintetizem o que você aprendeu sobre Python até
# agora. Comece cada linha com a expressão Em Python podemos.... Salve o
# arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios
# deste capítulo. Escreva um programa que leia o arquivo e mostre o que você
# escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez
# percorrendo o objeto arquivo com um laço e outra armazenando as linhas em uma
# lista e então trabalhando com ela fora do bloco with.
# filename = 'learning_python.txt'

file_path = r'C:\Users\lelena\Documents\curso-python\pt1\cap10_arquivos_e_exceções\learning_python.txt'

# lendo o arquivo todo
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

#pecorrendo o arquivo com um laço
with open(file_path) as file_object:
    for line in file_object:
        print(line)


#armazenando a file em uma lista e trabalhando com ela fora do bloco with
with open(file_path) as file_object:
    lines = file_object.readlines() #.readlines() armazena a file em uma lista

for line in lines:
    print(line)