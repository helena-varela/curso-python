# 9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva uma classe
# chamada Admin que herde da classe User escrita no Exercício 9.3 (página 226),
# ou no Exercício 9.5 (página 232). Adicione um atributo privileges que armazene
# uma lista de strings como "can add post", "can delete post" "can ban user",
# e assim por diante. Escreva um método chamado show_privileges() que liste o
# conjunto de privilégios de um administrador. Crie uma instância de Admin e chame
# seu método.

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

class Admin(User):
    def __init__(self, first_name, last_name, username, email, country):
        super().__init__(first_name, last_name, username, email, country)
        self.atributos_privelege = ['can add posts', 'can delete posts','can ban users'] 

    def show_priveleges(self):
        """Exibe os previlégios de Admin"""
        print('An admin:')
        for privelege in self.atributos_privelege:
            print(privelege)
    
admin1 = Admin('fulano','silva','fulano.45','fulano@gmail.com','brasil')
admin1.show_priveleges()