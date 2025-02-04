# 7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
# ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
# anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, 
# o ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso 
# custará 15 dólares. Escreva um laço em que você pergunte a idade aos usuários 
# e, então, informe-lhes o preço do ingresso do cinema.
texto = ("\t Qual a sua idade?" )    
texto += ("\n Escreva 'quit' para terminar a sessão. ")

while True:
    age = input(texto)
    if age ==  'quit':
        break
    if int(age) < 3: 
        print("Gratuito")
    elif int(age) >= 3 and int(age) <= 12: 
        print("10 dólares")
    elif int(age) > 12:
        print("15 dólares")
