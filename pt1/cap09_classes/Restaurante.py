"""Classe que representa um restaurante"""
class Restaurant():
    def __init__(self, name, type):
        """Nome e tipo do restaurante"""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        """Descreve o restaurante mostrando as informações de nome  e type"""
        print(f"O nome do restaurante é {self.name.title()} e trabalha no ramo de {self.type}.")

    def open_restaurante(self):
        """Exibe que o restaurannte está aberto"""
        print(f"O restaurante {self.name.title()} está aberto.\n")