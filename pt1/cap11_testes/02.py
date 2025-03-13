# 11.2 – População: Modifique sua função para que ela exija um terceiro
# parâmetro, population. Agora ela deve devolver uma única string no formato
# Cidade, País – população xxx, por exemplo, Santiago, Chile – população
# 5000000. Execute test_cities.py novamente. Certifique-se de que
# test_city_country() falhe dessa vez.
# Modifique a função para que o parâmetro population seja opcional. Execute
# test_cities.py novamente e garanta que test_city_country() passe novamente.
# Escreva um segundo teste chamado test_city_country_population() que
# verifique se você pode chamar sua função com os valores 'santiago', 'chile' e
# 'population=5000000'. Execute test_cities.py novamente e garanta que esse novo
# teste passe.

import unittest
from city_functions2 import formatted_address2

class CityTestCase(unittest.TestCase):
    def test_city_country_population(self): #importante ter test_ no inicio do nome da função
        data = formatted_address2('santiago','chile','500000')
        self.assertEqual(data, 'Santiago, Chile - 500000')

unittest.main()