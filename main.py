from pprint import pprint

from logic import *


def main():
    """
    Функция для вывода
    :return:
    """
    result = get_points('uuee', 'urml')
    pprint(result, compact=True, width=105)


if __name__ == '__main__':
    main()
