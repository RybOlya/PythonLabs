from models.education_level import EducationLevel
from models.form_of_education import FormOfEducation
from models.group import Group
from models.institute import Institute
from models.schedule import Schedule
from models.student import Student
from models.university import University


def main():
    martha_batkovets = Student("Martha", "Batkovets","Volodymyrivna","NULP", "IKTA",EducationLevel.BACHELOR,"IoT", FormOfEducation.FULL_TIME,"IR",14,2023,4.4)
    oleh_delych = Student("Oleh", "Delych","Maksymovuch","NULP", "IKTA",EducationLevel.BACHELOR,"IoT", FormOfEducation.FULL_TIME,"IR",14,2023,3.4)
 
    students_IR = {martha_batkovets,oleh_delych}
    group_IR = Group("NULP", "IKTA","Iot","IR",14,students_IR)
    print(martha_batkovets)
    print(martha_batkovets.student_performance())
    print(oleh_delych)
    print(oleh_delych.student_performance())
    lectures = {"mon":["Сircuitry","Math"],
                "tue":["Math","Сircuitry","History"],
                "wed":["History","Сircuitry"],
                "thu":["Discrete Math","Programming","Programming"],
                "fri":["English","Discrete Math"]}
    
    schedule_IR = Schedule(lectures)
    print(schedule_IR)
if __name__ == "__main__":
    main()
