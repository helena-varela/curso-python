# 10.7 – Calculadora para adição: Coloque o código do Exercício 10.6 em um
# laço while para que o usuário possa continuar fornecendo números, mesmo se
# cometerem um erro e digitarem um texto no lugar de um número.

while True:
    print('Escolha dois números para somar:\nDigete "sair" para fechar o programa.\n')

    n1 = (input('Primeiro número: '))
    if n1 == 'sair':
            break
    n2 = (input('Segundo número: '))
    if n2 == 'sair':
        break 
    try: #try tem que estar posicionado onde será gerado um erro
        soma = int(n1) + int(n2)
    except ValueError: #se gerar um erro, except tratara o erro
        print('\nO programa aceita apenas números para realizar a soma.\nTente novamente.\n')
    else: print(f'\nO resultado será: {soma} \n')

#finally - executara mesmo com o except e try dando certo ou errado