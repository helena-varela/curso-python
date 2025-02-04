#4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em
#seguida, use min() e max() para garantir que sua lista realmente começa em um e
#termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com
#que Python é capaz de somar um milhão de números
numeros = list(range(1, 1000001))
print(min(numeros))
print(max(numeros))
print(sum(numeros))