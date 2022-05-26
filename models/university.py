class University:

    def __init__(self, university_name: str) -> None:

        self._university_name = university_name

    def __str__(self) -> str:
        return f"{self._university_name}"