import requests
from bs4 import BeautifulSoup as Bs


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
        if requests.post(url, data=data).status_code == 200:
            html = requests.post(url, data=data)
            return html.text
    except Exception as error_code:
        raise error_code


def get_point(html: str) -> list[list[str]]:
    """
    Функция для получения пролетаемых точек
    :param html:
    :return: Список, состоящий из списка строк со значениями точек
    """
    points_path = []
    soup = Bs(html, 'html.parser')
    path = (str(soup.find('pre'))).split('\n')[1:-1]
    for i in path:
        if len(i.split()) == 6:
            modified_path = (
                        i.split()[0] + " None " + ' '.join(i.split()[1:]).replace("'", "M").replace('"', 'S')).split()
            points_path.append(modified_path)
        else:
            points_path.append(i.split())
    return points_path


def main():
    """
    Функция для вывода
    :return:
    """
    print(get_point(get_html('uuee', 'urml')))
