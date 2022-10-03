from models.university import University
from models.university_name import UniversityName

class Institute(University):

    def __init__(self, university_name: UniversityName, faculty: str, groups: list) -> None:

        super().__init__(university_name)
        self._faculty = faculty
        self._groups = groups

    def __str__(self) -> str:
        return super().__str__()+ f" {self._faculty}"
