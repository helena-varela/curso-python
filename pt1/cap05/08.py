#5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o
#nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma
#saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista
#com um laço e mostre uma saudação para cada usuário:
#• Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo,
#Olá admin, gostaria de ver um relatório de status?
#• Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por
#fazer login novamente.

usuarios = ['admin','maria','joao','fulano','ciclano']
for usuario in usuarios:
    if usuario == 'admin':
        print('Olá, admin, gostaria de um relatório de status?')
    else: 
        print('Olá, ' + str(usuario) + ', obrigado por fazer login novamente')