#7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
#número é múltiplo de dez ou não.

numero = input('Diga um número: ')
print(numero)
numero = int(numero)

if numero % 10 == 0 :
    print('É múltiplo de 10!')
else: print('Não é múltiplo de 10.')