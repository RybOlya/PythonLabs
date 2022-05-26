from models.university import University


class Institute(University):

    def __init__(self, university_name: str, faculty: str) -> None:

        super().__init__(university_name)
        self._faculty = faculty

    def __str__(self) -> str:
        return super().__str__()+ f" {self._faculty} "
