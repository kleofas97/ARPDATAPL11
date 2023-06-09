"""
    Napisz prosta funkcje "szyfrujaca". Jej zadaniem jest zamiana
    co trzeciego znaku w hasle na znak gwiazdki (*).
    Przyklad:
    >> x = hide_password("moje_super_tajne_haslo123")
    >> print(x)
    "mo*e_*up*r_*aj*e_*as*o1*3"
    Pamietaj, ze dlugosc napisu nie musi byc podzielna przez 3.
"""


def hide_password(password: str) -> str:
    """Ukrywa co trzecia litere w hasle password.
    :param password: haslo z gwiazdkami co trzecia litere.
    :return: napis z czesciowo ukrytym haslem.
    """
    new_password = ''

    for index, litera in enumerate(password):
        if (index + 1) % 3 == 0:  # tez pasuje index % 3 == 2
            new_password += '*'
        else:
            new_password += litera
    return new_password
