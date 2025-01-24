#4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços
#for para fazer exibições a fim de economizar espaço. Escolha uma versão de
#foods.py e escreva dois laços for para exibir cada lista de comidas.
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
my_foods.append('cannoli')
friends_foods.append('ice cream')

print('minhas comidas favoritas: ')
for my_food in my_foods:
    print(str(my_food))

print('\ncomidas favoritas do meu amg: ')
for friendsfood in friends_foods:
    print(str(friendsfood))