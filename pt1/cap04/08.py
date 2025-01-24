#4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por
#exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
#primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
#para exibir o valor de cada cubo.
cubos = [ ]
for valor in range(1,11):
    cubo = valor**3
    cubos.append(cubo)
print(cubos)

