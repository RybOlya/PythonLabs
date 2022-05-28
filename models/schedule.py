
class Schedule():

    def __init__(self, disciplines: dict):
        self._disciplines = disciplines

    def __str__(self) -> str:
        return f"{ str(self._disciplines.items())}"