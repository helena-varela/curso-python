# 10.9 – Gatos e cachorros silenciosos: Modifique o seu bloco except do Exercício
# 10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.

dogs = r'C:\Users\lelena\Documents\curso-python\pt1\cap10_arquivos_e_exceções\dogs.txt'
# cats = r'C:\Users\lelena\Documents\curso-python\pt1\cap10_arquivos_e_exceções\cats.txt'

try:
    with open(dogs) as object:     
        arquivo = object.read()

    with open('cats.txt') as object:  
        arquivo2 = object.read()

except FileNotFoundError:
    pass

else: print('Cachorros:\n' + arquivo.title() + '\n') 
# print('Gatos:\n' + arquivo2.title() + '\n')