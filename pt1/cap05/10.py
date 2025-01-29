#5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa
#que simule o modo como os sites garantem que todos tenham um nome de usuário único.
#• Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
#• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que
#um ou dois dos novos usuários também estejam na lista current_users.
#• Percorra a lista new_users com um laço para ver se cada novo nome de usuário
#já foi usado. Em caso afirmativo, mostre uma mensagem informando que a
#pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado,
#apresente uma mensagem dizendo que o nome do usuário está disponível.
#• Certifique-se de que sua comparação não levará em conta as diferenças entre
#letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá ser aceito.

current_users = ['fulano', 'ciclano','beltrano','joao','maria']
new_users = ['joao','MARIA','laura','larissa','fernanda']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('esse usuário já existe')
    else: print('usuário disponível')