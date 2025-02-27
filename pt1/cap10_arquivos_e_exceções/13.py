# 10.13 – Verificando se é o usuário correto: A última listagem de
# remember_me.py supõe que o usuário já forneceu seu nome ou que o programa
# está executando pela primeira vez. Devemos modificá-lo para o caso de o usuário
# atual não ser a pessoa que usou o programa pela última vez.
# Antes de exibir uma mensagem de boas-vindas de volta em greet_user(),
# pergunte ao usuário se seu nome está correto. Se não estiver, chame
# get_new_username() para obter o nome correto.

import json

def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("Qual o seu nome? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_stored_username()
    correto = input(f"Verifique se seu nome está correto: {username}\n(sim/não)\n")
    if correto == "sim":
        print(f"Seja bem-vindo de volta, {username}!")
    else:
        username = get_new_username()
        print(f"Lembrarei de você quando você voltar, {username}!")

greet_user()