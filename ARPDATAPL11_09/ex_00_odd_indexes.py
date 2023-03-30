# napisz funkcje ktora najpierw sprawdzi czy input jest stringiem
# a potem zwroci co druga litere, zaczynajac od 2 litery


def odd_indexes(tekst: str):
    if isinstance(tekst, str):
        return tekst[1::2]
    return None  # ewentualnie '' (pusty string)


if __name__ == "__main__":
    print(odd_indexes('Tester'))
    # 'Teleturniej' -> 'eeune'
    # 'Tekst' -> 'es'
