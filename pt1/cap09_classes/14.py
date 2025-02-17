# 9.14 – Dados: O módulo random contém funções que geram números aleatórios
# de várias maneiras. A função randint() devolve um inteiro no intervalo
# especificado por você. O código a seguir devolve um número entre 1 e 6:
# from random import randint x = randint(1, 6)
# Crie uma classe Die com um atributo chamado sides, cujo valor default é 6.
# Escreva um método chamado roll_die() que exiba um número aleatório entre 1 e
# o número de lados do dado. Crie um dado de seis dados e lance-o dez vezes.
# Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez vezes

from random import randint
import random 

class Die():
    def __init__(self, sides = 6): #valor de lados default = 6
        self.sides = sides 

    def roll_die(self):
        X = random.randint(1, self.sides) #armazena numa variável um número aleatório entre 1 e o número de lados do dado
        print(X)

print('Dado de 6 lados:')
dado6 = Die()
dado6.roll_die()

print('Dado de 10 lados:')
dado10 = Die(10)
dado10.roll_die()

print('Dado de 20 lados')
dado20 = Die(20)
dado20.roll_die()