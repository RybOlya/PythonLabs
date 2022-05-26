class Performance():


    def __init__(self, average_score: float):

               self._average_score = average_score

    def __str__(self) -> str:
        return super().__str__() + f"Average score is {self._average_score}."

    def student_performance1(self) -> str:
        if self._average_score == 5:
            return "Perfect"
        if 4.5 <= self._average_score < 5:
            return "Very good"
        if 3.5 <= self._average_score < 4.5:
            return "Good"
        if 3 <= self._average_score < 3.5:
            return "Satisfactory"
        if self._average_score < 3:
            return "Unsatisfactory"