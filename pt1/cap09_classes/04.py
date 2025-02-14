# 9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
# 225). Acrescente um atributo chamado number_served cujo valor default é 0. Crie
# uma instância chamada restaurant a partir dessa classe. Apresente o número de
# clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o
# novamente.
# Adicione um método chamado set_number_served() que permita definir o
# número de clientes atendidos. Chame esse método com um novo número e mostre o
# valor novamente.
# Acrescente um método chamado increment_number_served() que permita
# incrementar o número de clientes servidos. Chame esse método com qualquer
# número que você quiser e que represente quantos clientes foram atendidos, por
# exemplo, em um dia de funcionamento.

class Restaurant():
    def __init__(self, name, type):
        """Atributos que descrevem o restaurante"""
        self.name = name
        self.type = type
        self.number_served = 0 #número default

    def describe_restaurant(self):
        """Descreve o restaurante mostrando as informações de nome  e type"""
        print(f"O nome do restaurante é {self.name.title()}, trabalha no ramo de {str(self.type)}.")

    def open_restaurante(self):
        """Exibe que o restaurannte está aberto"""
        print(f"O restaurante {self.name.title()} está aberto.")

    def show_served(self):
        """Exibirá o número de clientes"""
        print(f"O número de clientes atendidos foi de {self.number_served}")

    def set_number_served(self, clientes):
        """Modificará o número de clientes atendidos"""
        self.number_served = clientes #aceite um parâmetro para modificar number_served

    def increment_number_served(self,clientes):
        """Soma ao valor de clientes atendidos"""
        self.number_served += clientes #aceita um parâmetro que soma ao número de number_served

restaurant = Restaurant('nau','frutos do mar',)
restaurant.describe_restaurant()
restaurant.open_restaurante()
restaurant.show_served() #número de clientes antes de modificar

restaurant.number_served = 100 #muda diretamente o atributo de ___init___
restaurant.show_served() #número de clientes depois de modificar

restaurant.set_number_served(150) #muda o atributo através de um método
restaurant.show_served()

restaurant.increment_number_served(100) #soma 100 ao número de clientes
restaurant.show_served()