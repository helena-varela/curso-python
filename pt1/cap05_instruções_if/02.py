#5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
#criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescenteos em conditional_tests.py. Tenha pelo menos um resultado True e um False para
#cada um dos casos a seguir:
#• testes de igualdade e de não igualdade com strings;
#• testes usando a função lower();
#• testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
#maior ou igual a e menor ou igual a;
#• testes usando as palavras reservadas and e or;
#• testes para verificar se um item está em uma lista;
#• testes para verificar se um item não está em uma lista.
print('Comparando strings')
color = 'green'
print("é verde")
print(color == 'green')
print('nao é verde')
print(color == 'blue')

print('Função lower')
carro = 'Toyota'
carro.lower() == 'toyota'

print('Teste de função lower na lista')
cars = ['Toyota','bmw','Subaru','Audi']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: print(car.lower())

print('Igualdade de numeros')
age = 21
print(age == 21) #true
print(age < 23) #true
print(age > 25) #false
print(age >= 21) #true
print(age >= 22) #false

print('Usando and')
uni1 = 14
uni2 = 18
print(uni1 >= 15) and (uni2 >= 15)

print('Usando or')
print(uni1 < 16) or (uni2 <16)

print('Se o item está na lista')
lista = ['cachorro','gato','coelho']

if "cachorro" in lista:
    print('cachorro esta na lista')

if 'cavalo' not in lista:
    print('cavalo nao esta na lista')