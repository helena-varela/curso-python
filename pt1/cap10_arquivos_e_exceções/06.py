# 10.6 – Adição: Um problema comum quando pedir entradas numéricas ocorre
# quando as pessoas fornecem texto no lugar de números. Ao tentar converter a
# entrada para um int, você obterá um TypeError. Escreva um programa que peça
# dois números ao usuário. Some-os e mostre o resultado. Capture o TypeError caso
# algum dos valores de entrada não seja um número e apresente uma mensagem de
# erro simpática. Teste seu programa fornecendo dois números e, em seguida, digite
# um texto no lugar de um número.

print('Escolha dois números para somar:\nDigete "sair" para fechar o programa.\n')

n1 = (input('Primeiro número: '))
n2 = (input('Segundo número: '))

try: #try tem que estar posicionado onde será gerado um erro
    soma = int(n1) + int(n2)
except ValueError: #se gerar um erro, except tratara o erro
    print('\nO programa aceita apenas números para realizar a soma.\nTente novamente.\n')
else: print(f'\nO resultado é: {soma}\n')