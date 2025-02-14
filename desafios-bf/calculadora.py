# Implemente uma calculadora, que faça todas as operações com apenas dois número, exemplos:
# - Soma (1 + 1) => 2
# - Subtração (7 - 9) => -2
# - Divisão (100 / 2) => 50
# - Multiplicação (22 * 10) => 220
def soma():
    resultado = n1 + n2
    print("O resultado será: ",resultado)

def subtração():
    resultado = n1 - n2
    print("O resultado será: ",resultado)
def multiplicação():
    resultado = n1 * n2
    print("O resultado será: ",resultado)
def divisão():
    resultado = n1 // n2
    print("O resultado será: ",resultado)

while True:
    print("_" * 30)
    print("\nBEM-VINDO A CALCULADORA")
    print("_" * 30)
    print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
    operação = input('Qual operação você deseja fazer? \nEscolha uma das opções.\nSe desejar finalizar os cálculos, digite "sair". \n')
    if operação == "sair": 
        break
    n1 = int(input("Diga dois números para realizar a operação:\n"))
    n2 = int(input())
    if operação == "1":
        soma()
    elif operação == "2":
        subtração()
    elif operação == "3":
        multiplicação()
    elif operação == "4": 
        divisão()