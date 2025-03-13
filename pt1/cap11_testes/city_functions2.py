def formatted_address2(city, country, population = ''):
    """A função devolve uma string no formato: Cidade, País - População"""
    if population:
        address = city +', ' + country + ' - ' + str(population)
    else:
        address = city + ', ' + country
    return address.title()
