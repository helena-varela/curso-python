#7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
#quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
#exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
#contrário, informe que sua mesa está pronta.

reserva = input('Quantas pessoas estão em seu grupo para jantas? ')
print(reserva)
reserva = int(reserva)

if reserva > 8:
    print('Vocês deverão esperar uma mesa.')
else: print('Sua mesa está pronta!')