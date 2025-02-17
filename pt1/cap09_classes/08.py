# 9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
# atributo privileges que armazene uma lista de strings conforme descrita no
# Exercício 9.7 OK. Transfira o método show_privileges() para essa classe OK. Crie uma
# instância de Privileges como um atributo da classe Admin. Crie uma nova
# instância de Admin e use seu método para exibir os privilégios.

class User():
    def __init__(self, first_name, last_name, username, email, country):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.country = country.title()

    def describe_user(self):
        print(f"Primeiro nome: {self.first_name}\nÚltimo nome: {self.last_name}\nUsername: {self.username}\nEmail: {self.email}\nPaís: {self.country}\n")

    def greet_user(self):
        print(f"Olá, {self.username}, seja bem-vindo!\n")

class Previleges(): #criação da classe Previleges
    def __init__(self): 
        self.privileges = ['can add posts', 'can delete posts','can ban users'] #atributo com uma lista citando seus previlégios

    def show_priveleges(self): #função que lista esses previlégios
        """Exibe os previlégios de Admin"""
        print('An admin:')
        for privelege in self.privileges:
            print(privelege)

class Admin(User):
    def __init__(self, first_name, last_name, username, email, country):
        super().__init__(first_name, last_name, username, email, country)
        self.previleges = Previleges() #cria-se um atributo e a instância será a classe Previleges()

admin1 = Admin('fulano','silva','fulano.45','fulano@gmail.com','brasil')
admin1.previleges.show_priveleges() #chama a função da classe Previleges()

