# 11.3 – Funcionário: Escreva uma classe chamada Employee. O método
# __init__() deve aceitar um primeiro nome, um sobrenome e um salário anual, e
# deve armazenar cada uma dessas informações como atributos. Escreva um método
# de nome give_raise() que some cinco mil dólares ao salário anual, por default,
# mas que também aceite um valor diferente de aumento.
# Escreva um caso de teste para Employee. Crie dois métodos de teste,
# test_give_default_raise() e test_give_custom_raise(). Use o método
# setUp() para que não seja necessário criar uma nova instância de funcionário em
# cada método de teste. Execute seu caso de teste e certifique-se de que os dois
# testes passem.
import unittest

class Employee():
    def __init__(self,first_name,surname,annual_salary):
        self.first_name = first_name
        self.surname = surname
        self.annual_salary = annual_salary

    def give_raise(self, acrescimo = 5000):
        with_raise = self.annual_salary + acrescimo
        return with_raise

# pessoa = Employee('helena','varela',1000)
# pessoa.give_raise(500)

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.pessoa = Employee('fulano','da silva',1000)

    
    def test_give_default_raise(self):
        self.pessoa.give_raise()


    def test_give_custom_raise(self):
        self.pessoa.give_raise(500)

unittest.main()