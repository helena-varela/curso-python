#6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
#(página 147). Crie dois novos dicionários que representem pessoas diferentes e
#armazene os três dicionários em uma lista chamada people. Percorra sua lista de
#pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
#sabe sobre cada pessoa.

pessoa1 = {'first_name': 'joão',
          'last_name':'camboim', 
          'age': 20, 
          'city':'joão pessoa',
          }

pessoa2 = {'first_name':'helena',
           'last_name': 'guanaes',
           'age': 19,
           'city':'natal',
           }

pessoa3 = {'first_name': 'juliana',
           'last_name':'araújo',
           'age': 18,
           'city': 'natal',
           }

people = [pessoa1, pessoa2, pessoa3 ]

for person in people:
    print(person)
   