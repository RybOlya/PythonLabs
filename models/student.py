from models.education_level import EducationLevel
from models.form_of_education import FormOfEducation
from models.performance import Performance


class Student():

    def __init__(self, first_name: str, last_name: str, middle_name: str, education_level: EducationLevel, 
                form_of_study: FormOfEducation,  graduation_year: str, average_score: float) -> None:

        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._education_level = education_level
        self._form_of_study = form_of_study
        self._graduation = graduation_year
        self._performance = Performance(average_score)

    def __str__(self) -> str:
        return f"{self._last_name} {self._first_name} {self._middle_name}"

    def student_performance(self) -> str:
        return f"Student has {Performance.student_performance(self._performance)} performance"
