#4.2 – Animais: Pense em pelo menos três animais diferentes que tenham uma
#característica em comum. Armazene os nomes desses animais em uma lista e,
#então, utilize um laço for para exibir o nome de cada animal.
#• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo,
#Um cachorro seria um ótimo animal de estimação.
#• Acrescente uma linha no final de seu programa informando o que esses animais
#têm em comum. Você poderia exibir uma frase como Qualquer um desses
#animais seria um ótimo animal de estimação!
animais = ['coelho', 'cachorro','gato']
for animal in animais:
    print(animal)

for animal in animais:
    print('um ' + animal + ' é um ótimo animal de estimação\n')

for animal in animais:
    print(animal + " é peludinho e fofinho\n")
    
print('qualquer um desses animais seria um otimo animal de estimação')
