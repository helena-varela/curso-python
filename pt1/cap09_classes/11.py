# 9.11 – Importando Admin: Comece com seu programa do Exercício 9.8 (página
# 241). Armazene as classes User, Privileges e Admin em um módulo. Crie um
# arquivo separado e uma instância de Admin e chame show_privileges() para
# mostrar que tudo está funcionando de forma apropriada.

from Usuário import User, Previleges, Admin

admin1 = Admin('fulano','silva','fulano.45','fulano@gmail.com','brasil')
admin1.previleges.show_priveleges() 