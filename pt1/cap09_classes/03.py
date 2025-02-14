# 9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
# first_name e last_name e, então, crie vários outros atributos normalmente
# armazenados em um perfil de usuário. Escreva um método de nome
# describe_user() que apresente um resumo das informações do usuário. Escreva
# outro método chamado greet_user() que mostre uma saudação personalizada ao
# usuário.
# Crie várias instâncias que representem diferentes usuários e chame os dois
# métodos para cada usuário.

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

user1 = User('fulano','silva','fulano.45','fulano@gmail.com','brasil')
user1.describe_user()
user1.greet_user()

user2 = User('ciclano','medeiros','ciclano_medeiros','ciclanomd@gmail.com','portugal')
user2.describe_user()
user2.greet_user()

user3 = User('beltrano','carvalho','beltrano.carvalho22','beltrano@gmail.com','cabo verde')
user3.describe_user()
user3.greet_user()
