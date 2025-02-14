# 9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
# instâncias diferentes da classe e chame describe_restaurant() para cada
# instância.

class Restaurant():
    def __init__(self, name, type):
        """Nome e tipo do restaurante"""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        """Descreve o restaurante mostrando as informações de nome  e type"""
        print(f"O nome do restaurante é {self.name.title()} e trabalha no ramo de {self.type}.")

    def open_restaurante(self):
        print(f"O restaurante {self.name.title()} está aberto.\n")
    
restaurant1 = Restaurant('nau','frutos do mar')
restaurant1.describe_restaurant()
restaurant1.open_restaurante()

restaurant2 = Restaurant('YoshiYa', 'comida japonesa')
restaurant2.describe_restaurant()
restaurant2.open_restaurante()

restaurant3 = Restaurant('sicília', 'comida italiana')
restaurant3.describe_restaurant()
restaurant3.open_restaurante()