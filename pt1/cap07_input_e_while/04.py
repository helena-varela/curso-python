#7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
#fornecer uma série de ingredientes para uma pizza até que o valor 'quit' 
# seja fornecido. À medida que cada ingrediente é especificado, apresente uma
#mensagem informando que você acrescentará esse ingrediente à pizza.

texto = "\t Quais ingredientes vc quer? " 
texto += "\n Enter 'quit' para finalizar o pedido. "

while True:
    pedido = input(texto)
    if pedido == 'quit':
        break
    else: 
        print("O ingrediente: " + pedido + " foi adicionado a pizza!")