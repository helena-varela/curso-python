# 10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário.
# Quando ele responder, escreva o nome em um arquivo chamado guest.txt.

file_path = r'C:\Users\lelena\Documents\curso-python\pt1\cap10_arquivos_e_exceções\guest.txt'
nome = input('Qual o seu nome? ')

with open(file_path, 'w') as file_object:
    file_object.write(nome.title())