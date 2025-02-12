# 8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
# 210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome e
# o sobrenome, além de três outros pares chave-valor que o descrevam

def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Helena', 'Varela', age=19,  city = 'Natal', gender = 'fem')
print(user_profile)