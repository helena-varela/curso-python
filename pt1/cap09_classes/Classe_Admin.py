from Classe_User import User

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