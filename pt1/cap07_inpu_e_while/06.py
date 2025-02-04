# 7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do 
# Exercício 7.5 que faça o seguinte, pelo menos uma vez:
# • use um teste condicional na instrução while para encerrar o laço;
# • use uma variável active para controlar o tempo que o laço executará;
# • use uma instrução break para sair do laço quando o usuário fornecer 
# o valor 'quit'.

texto = ("\t Qual a sua idade?" )    
texto += ("\n Escreva 'quit' para terminar a sessão. ")

#Variável active:
active = True
while active:
    age = input(texto)
    if age ==  'quit':
        active = False
    if int(age) < 3: 
        print("Gratuito")
    elif int(age) >= 3 and int(age) <= 12: 
        print("10 dólares")
    elif int(age) > 12:
        print("15 dólares")

#Dar break se o usuário fornecer o valor 'quit':
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