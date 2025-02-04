# 7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
# férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
# visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
# apresente os resultados da enquete.

resultados = {}

enquete = True
while enquete:
    name = input('Qual seu nome? ')
    resposta = input('\nSe pudesse visitar um lugar do mundo, para onde você iria? ')
    resultados[name] = resposta
    continuar = input('\n Deseja terminar a enquete? ')
    if continuar == 'sim':
        enquete = False

print('\nResultados da enquete:\n')
for name, resposta in resultados.items():
    print(str(name.title()) + ' gostaria de ir para ' + str(resposta.title()) + '.\n')
