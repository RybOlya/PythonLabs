from models.education_level import EducationLevel
from models.form_of_education import FormOfEducation
from models.group import Group
from models.performance import Performance


class Student(Group):

    def __init__(self, first_name: str, last_name: str, middle_name: str, university_name: str, faculty: str, education_level: EducationLevel, 
                 major: str, form_of_study: FormOfEducation, group_name: str, group_number: str, graduation_year: str, average_score: float) -> None:

        super().__init__(university_name, faculty, major, group_name, group_number,0)
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._education_level = education_level
        self._form_of_study = form_of_study
        self._graduation = graduation_year
        self._performance = Performance(average_score)

    def __str__(self) -> str:
        return f"{self._last_name, self._first_name, self._middle_name} is currently attending " + super().__str__()

    def student_performance(self) -> str:
        return f"Student has {Performance.student_performance1(self._performance)} performance"
