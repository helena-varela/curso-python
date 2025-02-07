# 8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
# Escreva um laço while que permita aos usuários fornecer o nome de um artista e o
# título de um álbum. Depois que tiver essas informações, chame make_album() com
# as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um
# valor de saída no laço while.

def make_album(artista, titulo, n_faixas = ''):
    """"devolve um dicionário"""
    repertorio = {'Cantor':artista.title(), 'Album': titulo.title(), 'Número de faixas': n_faixas}
    if n_faixas: 
        repertorio['Número de faixas']=n_faixas
    return repertorio

while True:
    print('\tPor favor complete o formulário \n Digite "sair" se desejar finalizar as perguntas.')
    ct = input("Cantor: ")
    if ct == 'sair':
        break
    ab = input("Album: ")
    if ab == 'sair':
        break
    n_fx = int(input("Número de faixas: "))
    if n_fx == 'sair':
        break
    fazer_album = make_album(ct, ab, n_fx)
    print(fazer_album)