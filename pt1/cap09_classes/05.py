# 9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à sua
# classe User do Exercício 9.3 (página 226). Escreva um método chamado
# increment_login_attempts() que incremente o valor de login_attempts em 1.
# Escreva outro método chamado reset_login_attempts() que reinicie o valor de
# login_attempts com 0.
# Crie uma instância da classe User e chame increment_login_attempts()
# várias vezes. Exiba o valor de login_attempts para garantir que ele foi
# incrementado de forma apropriada e, em seguida, chame
# reset_login_attempts(). Exiba login_attempts novamente para garantir que
# seu valor foi reiniciado com 0.

class User():
    def __init__(self, login_attempts):
        self.login_attempts = 0 #número default

    def increment_login_attempts(self, login):
        """Incrementa o valor de login em 1"""
        self.login_attempts += login
        print(f"Mais {self.login_attempts} tentativas de login.")

    def reset_login_attempts(self):
        """Reseta as tentativas de login para 0"""
        self.login_attempts = 0
        print(f"Sua tentiva de login foi resetada para {self.login_attempts}")

user1 = User(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.reset_login_attempts()