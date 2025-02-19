# 10.4 – Lista de convidados: Escreva um laço while que pergunte o nome aos
# usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
# acrescente uma linha que registre a visita do usuário em um arquivo chamado
# guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
# arquivo.
file_path = r'C:\Users\lelena\Documents\curso-python\pt1\cap10_arquivos_e_exceções\guest_book.txt'

while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}, seja bem-vindo!\n')
    
    with open(file_path,'a') as file_object:
        file_object.write(nome.title() + '\n')