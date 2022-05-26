from models.group import Group

class Schedule(Group):

    def __init__(self, disciplines: dict):
        self._disciplines = disciplines

    def __str__(self) -> str:
        return f"{ str(self._disciplines.items())}"