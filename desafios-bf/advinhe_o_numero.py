import random
while True:
    numero = random.randint(0,10)

    while True:
        resposta = int(input('Advinhe o número entre 0 e 10: '))
        if resposta == numero:
            print('Parabéns, você acertou!')
            continuar = input('Deseja reiniciar o jogo? ')
            if continuar == 'sim':
                break
            else: exit()
        elif resposta < numero: print('Muito baixo!')
        elif resposta > numero: print('Muito alto!')