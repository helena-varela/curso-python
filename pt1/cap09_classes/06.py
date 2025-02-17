# 9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma
# classe chamada IceCreamStand que herde da classe Restaurant escrita no
# Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer versão da
# classe funcionará; basta escolher aquela de que você mais gosta. Adicione um
# atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva
# um método para mostrar esses sabores. Crie uma instância de IceCreamStand e
# chame esse método.

class Restaurant():
    def __init__(self, name, type):
        """Nome e tipo do restaurante"""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        """Descreve o restaurante mostrando as informações de nome  e type"""
        print(f"O nome do restaurante é {self.name.title()} e trabalha no ramo de {self.type}")

    def open_restaurante(self):
        """Exibe que o restaurannte está aberto"""
        print(f"O restaurante {self.name.title()} está aberto.\n")

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type = 'sorvetes')
        self.flavors = ['Chocolate','Menta', 'Ninho','Morango','Creme'] #adiciona flavors como um novo atributo

    def flavors_list(self):
        """Lista todos os sabores de sorvete"""
        print('A sorveteria conta com os sabores:')
        for flavor in self.flavors:
            print(flavor)

sorveteria1 = IceCreamStand(name='chiquinho',type = '')
sorveteria1.describe_restaurant()
sorveteria1.flavors_list()