# 9.12 – Vários módulos: Armazene a classe User em um módulo e as classes
# Privileges e Admin em um módulo separado. Em outro arquivo, crie uma instância
# de Admin e chame show_privileges() para mostrar que tudo continua
# funcionando de forma apropriada.

from Classe_User import User
from Classe_Admin import Admin, Previleges

admin1 = Admin('fulano','silva','fulano.45','fulano@gmail.com','brasil')
admin1.previleges.show_priveleges() 