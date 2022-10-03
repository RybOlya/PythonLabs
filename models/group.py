
from models.schedule import Schedule
class Group:

    def __init__(self, major: str, group_name: str, group_number:int, students: list, schedule: Schedule) -> None:
        
        self._major = major
        self._name = group_name
        self._number = group_number
        self._students = students
        self._schedule = schedule

    def __str__(self) -> str:
        return f"{self._name} {self._number} group has a schedule: {self._schedule}"