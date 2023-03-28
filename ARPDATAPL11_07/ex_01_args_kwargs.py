# args i kwargs.
# https://realpython.com/python-kwargs-and-args/
import sys


# modul do parsowania (po Bożemu)
# https://docs.python.org/3/library/argparse.html
# do powaznego stosowania -> biblioteka argparse


def arguments_args(*args):  # zapis gwiazdki 'opakowuje' wszystkie parametry do tuple'a
    # za pomoca *args moge przyjac dowolna liczbe argumentow do funkcji
    print(f'Jestem w funkcji {arguments_args.__name__}')
    print('Wypisuje wartosci argumentow:')
    for arg in args:
        print(arg)


def arguments_kwargs(**kwargs):
    # przyjmuje dowolna liczbe parametrow w formie dicta
    print(f'Jestem w funkcji {arguments_kwargs.__name__}')
    print('Wypisuje wartosci argumentow z kluczami:')
    for key in kwargs:
        print(f'for key {key}, value: {kwargs[key]}')


if __name__ == "__main__":
    n = len(sys.argv)

    # to samo co ponizej, w jednej linijce
    # for arg in sys.argv[1:]:
    #     arg.split('=')
    #     print(arg)

    kwargs = dict(arg.split('=') for arg in sys.argv[1:])
    print(kwargs)
    arguments_kwargs(**kwargs)
