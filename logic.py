import requests
from bs4 import BeautifulSoup as Bs

from models import *


def get_html(id_1: str, id_2: str) -> str:
    """
    Функция для отправки запроса и получения строки в html формате
    :param id_1:
    :param id_2:
    :return: HTML в формате текста(строки)
    """
    url = "https://rfinder.asalink.net/free/autoroute_rtx.php"
    data = {"id1": id_1,
            "ic1": "",
            "id2": id_2,
            "ic2": "",
            "minalt": "FL330",
            "maxalt": "FL330",
            "lvl": "B",
            "dbid": "2411",
            "usesid": "Y",
            "usestar": "Y",
            "easet": "Y",
            "rnav": "Y",
            "nats": "R",
            "k": "1929218769"}

    try:
        r = requests.post(url, data=data)
        if r.status_code == 200:
            html = r.text
            return html
    except Exception as error_code:
        raise error_code


def get_point(html: str) -> list[Fix]:
    """
    Функция для получения пролетаемых точек и их данных
    :param html:
    :return: Список, состоящий из точек id_
    """
    points = []
    soup = Bs(html, 'html.parser')
    table = soup.find('pre').text.split('\n')[1:-1]
    for i in table:
        columns = i.split()
        if len(columns) == 6:
            columns.insert(1, None)
        fix = Fix(*columns)
        points.append(fix)
    return points


def get_points(icao1: str, icao2: str) -> list[Fix]:
    """
    Функция для вызова функций(debug)
    :param icao1:
    :param icao2:
    :return:
    """
    # html = get_html(icao1, icao2)
    html = open('index.html').read()
    points = get_point(html)
    return points
