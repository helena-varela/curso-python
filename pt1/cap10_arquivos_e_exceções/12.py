# 10.12 – Lembrando o número favorito: Combine os dois programas do Exercício
# 10.11 em um único arquivo. Se o número já estiver armazenado, informe o número
# favorito ao usuário. Caso contrário, pergunte ao usuário qual é o seu número
# favorito e armazene-o em um arquivo. Execute o programa duas vezes para
# garantir que ele funciona.

import json

def armazena_numero():
    """Armazena o número"""
    try:
        with open('numero.json') as object:
            conteudo = json.load(object)
    except FileNotFoundError:
        print('Esse aquivo não existe')
    else: 
        return conteudo

def mostra_numero(): 
    """Verifica se há um número armazenado"""  
    conteudo = armazena_numero()
    if conteudo:            #se tiver um número armazenado ele irá mostrar qual é
        print(f'Eu sei qual o seu número favorito! É {conteudo}.')

    else:   #se não tiver o número armazenado ele irá perguntar qual é e armazenará em numero.json
        numero = input('Qual o seu número favorito? ')
        with open('numero.json','w') as object: 
            json.dump(numero, object) 
    
armazena_numero()
mostra_numero()