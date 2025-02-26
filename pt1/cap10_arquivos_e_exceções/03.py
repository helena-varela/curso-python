# 10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário.
# Quando ele responder, escreva o nome em um arquivo chamado guest.txt.

nome = input('Qual o seu nome? ')

with open('guest.txt', 'w') as file_object:
    file_object.write(nome.title())