"""Uma classe que representa um usuário"""
class User():
    def __init__(self, first_name, last_name, username, email, country):
        """Informações básicas de um usuário"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.country = country.title()

    def describe_user(self):
        """Descreve um usuário"""
        print(f"Primeiro nome: {self.first_name}\nÚltimo nome: {self.last_name}\nUsername: {self.username}\nEmail: {self.email}\nPaís: {self.country}\n")

    def greet_user(self):
        """Cumprimenta o usuário"""
        print(f"Olá, {self.username}, seja bem-vindo!\n")

class Previleges(): #criação da classe Previleges
    def __init__(self): 
        """Lista de privilégios"""
        self.privileges = ['can add posts', 'can delete posts','can ban users'] #atributo com uma lista citando seus previlégios

    def show_priveleges(self): #função que lista esses previlégios
        """Exibe os previlégios de Admin"""
        print('An admin:')
        for privelege in self.privileges:
            print(privelege)

class Admin(User):
    def __init__(self, first_name, last_name, username, email, country):
        """Criação da subclasse de User: Admin"""
        super().__init__(first_name, last_name, username, email, country)
        self.previleges = Previleges() #cria-se um atributo e a instância será a classe Previleges()