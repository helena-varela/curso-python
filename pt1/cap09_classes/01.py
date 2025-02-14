# 9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__()
# de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type.
# Crie um método chamado describe_restaurant() que mostre essas duas
# informações, e um método de nome open_restaurant() que exiba uma
# mensagem informando que o restaurante está aberto.
# Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois
# atributos individualmente e, em seguida, chame os dois métodos.

class Restaurant():
    def __init__(self, name, type):
        """Nome e tipo do restaurante"""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        """Descreve o restaurante mostrando as informações de nome  e type"""
        print(f"O nome do restaurante é {self.name.title()} e trabalha no ramo de {self.type}")

    def open_restaurante(self):
        print(f"O restaurante {self.name.title()} está aberto.\n")
    
restaurant = Restaurant('nau','frutos do mar')
restaurant.describe_restaurant()
restaurant.open_restaurante()

print(restaurant.name.upper())
print(restaurant.type)