#5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi
#feito no Exercício 5.3, e escreva uma cadeia if-else.
#• Se a cor do alienígena for verde, mostre uma frase informando que o jogador
#acabou de ganhar cinco pontos por atingir o alienígena.
#• Se a cor do alienígena não for verde, mostre uma frase informando que o
#jogador acabou de ganhar dez pontos.
#• Escreva uma versão desse programa que execute o bloco if e outro que execute o bloco else

alien_color = 'verde'
if alien_color == 'verde':
    print('voce ganhou 5 pontos por atingir o alienigena')

alien_color = 'verde'
if alien_color == 'vermelho':
    print('voce ganhou 5 pontos')
else: print('voce ganhou 10 pontos')    
  
