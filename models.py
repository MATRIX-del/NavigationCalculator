class Fix:
    # TODO В конструкторе прописать принятие всех характеристик точки
    #  и создать соответсвующие атрибуты (7 атрибутов)
    def __init__(self, id_: str, freq: str | None, trk: str, dist: str, coords1: str, coords2: str, name: str):
        """
        Инициализация
        :param id_:
        :param freq:
        :param trk:
        :param dist:
        :param coords1:
        :param coords2:
        :param name:
        """
        self.id_ = id_
        self.freq = freq
        self.trk = trk
        self.dist = dist
        self.coords1 = coords1
        self.coords2 = coords2
        self.name = name

    # TODO Вывод информации в виде:
    #  EMGAS None 181 92 N54&deg;27'28.00" E037&deg;50'19.00" EMGAS
    def __str__(self) -> str:
        """
        Функция, выводящая формат str
        :return:
        """
        return f"{self.id_} {self.freq} {self.trk} {self.dist} {self.coords1} {self.coords2} {self.name}"

    # TODO Вывод информации в виде:
    #  EMGAS
    def __repr__(self) -> str:
        """
        Функция, выводящая формат list
        :return:
        """
        return self.id_
