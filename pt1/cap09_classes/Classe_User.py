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