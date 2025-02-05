while True:
    numero = int(input('Advinhe o número entre 0 e 10: '))
    if numero == 7:
        print('Parabéns, você acertou!')
        continuar = input('Deseja continuar com o jogo? ')
        if continuar == 'sim':
            continue
        else: continuar == "nao" or "não"
        break
    elif numero < 7: print('Muito baixo!')
    elif numero >7: print('Muito alto!')
