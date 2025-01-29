#5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a
#lista de usuários não esteja vazia.
#• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários!
#• Remova todos os nomes de usuário de sua lista e certifique-se de que a mensagem correta seja exibida.

usuarios = ['admin','maria','joao','fulano','ciclano']
if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print('Olá, admin, gostaria de um relatório de status?')
        else: 
            print('Olá, ' + str(usuario) + ', obrigado por fazer login novamente')

usuarios = [ ]
if usuarios:
    for usuario in usuarios:
        print('Olá, ' + usuario + 'gostaria de um relatório de status?')
else: print('\nPreciamos encontrar alguns usuários!')