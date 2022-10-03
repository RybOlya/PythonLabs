from models.university_name import UniversityName
class University:

    def __init__(self, university_name: UniversityName) -> None:

        self._university_name = university_name

    def __str__(self) -> str:
        return f"{self._university_name}"