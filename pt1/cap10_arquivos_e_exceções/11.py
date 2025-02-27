# 10.11 – Número favorito: Escreva um programa que pergunte qual é o número
# favorito de um usuário. Use json.dump() para armazenar esse número em um
# arquivo. Escreva um programa separado que leia esse valor e apresente a
# mensagem “Eu sei qual é o seu número favorito! É _____.”.

import json

numero = input('Qual o seu número favorito? ')

with open('numero.json','w') as object: 
    json.dump(numero, object) 

with open('numero.json') as object:
    conteudo = json.load(object)

print(f'Eu sei qual o seu número favorito! É {conteudo}.')