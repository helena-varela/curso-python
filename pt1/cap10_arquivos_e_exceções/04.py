# 10.4 – Lista de convidados: Escreva um laço while que pergunte o nome aos
# usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
# acrescente uma linha que registre a visita do usuário em um arquivo chamado
# guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
# arquivo.

while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}, seja bem-vindo!\n')
    
    with open("guest_book.txt",'a') as file_object:
        file_object.write(nome.title() + '\n')