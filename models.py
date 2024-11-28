class Fix:
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

    def __str__(self) -> str:
        """
        Функция, выводящая формат str
        :return:
        """
        return f"{self.id_} {self.freq} {self.trk} {self.dist} {self.coords1} {self.coords2} {self.name}"

    def __repr__(self) -> str:
        """
        Функция, выводящая формат list
        :return:
        """
        return self.id_
