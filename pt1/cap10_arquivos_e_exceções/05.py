# 10.5 – Enquete sobre programação: Escreva um laço while que pergunte às
# pessoas por que elas gostam de programação. Sempre que alguém fornecer um
# motivo, acrescente-o em um arquivo que armazene todas as respostas

while True:
    pergunta = input('Por que você gosta de programação? \n')
    with open('enquete.txt', 'a') as file_object:
        file_object.write(pergunta.title() + '\n')