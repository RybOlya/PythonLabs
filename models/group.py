from models.institute import Institute


class Group(Institute):


    def __init__(self, university_name: str, faculty: str, major: str,
                 group_name: str, group_number:int, students: dict) -> None:

        super().__init__(university_name, faculty)
        self._major = major
        self._name = group_name
        self._number = group_number
        self._students = students

    def __str__(self) -> str:
        return super().__str__()+ f"in a {self._name, self._number} group"