def formatted_address(city, country):
    """A função devolve uma string no formato: Cidade, País"""
    address = city +', ' + country
    return address.title()