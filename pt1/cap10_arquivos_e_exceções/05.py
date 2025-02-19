# 10.5 – Enquete sobre programação: Escreva um laço while que pergunte às
# pessoas por que elas gostam de programação. Sempre que alguém fornecer um
# motivo, acrescente-o em um arquivo que armazene todas as respostas

path_file = r'C:\Users\lelena\Documents\curso-python\pt1\cap10_arquivos_e_exceções\enquete.txt'

while True:
    pergunta = input('Por que você gosta de programação? \n')
    with open(path_file, 'a') as file_object:
        file_object.write(pergunta.title() + '\n')