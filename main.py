from models.education_level import EducationLevel
from models.form_of_education import FormOfEducation
from models.university_name import UniversityName
from models.institute import Institute
from models.group import Group
from models.schedule import Schedule
from models.student import Student

def main():
    martha_batkovets = Student("Martha", "Batkovets","Volodymyrivna", EducationLevel.BACHELOR, FormOfEducation.FULL_TIME,2023,4.4)
    oleh_delych = Student("Oleh", "Delych","Maksymovuch",EducationLevel.BACHELOR, FormOfEducation.FULL_TIME,2023,3.4)
    students_IR = [martha_batkovets,oleh_delych]
    print(martha_batkovets)
    print(martha_batkovets.student_performance())
    print(oleh_delych)
    print(oleh_delych.student_performance())
    
    lectures = {"Mon":["Сircuitry","Math"],
                "tue":["Math","Сircuitry","History"],
                "wed":["History","Сircuitry"],
                "thu":["Discrete Math","Programming","Programming"],
                "fri":["English","Discrete Math"]}

    schedule_ir_14 = Schedule(lectures)
    group_ir_14 = Group("IoT","IR",14,students_IR,schedule_ir_14)
    print(group_ir_14)
    ikta_groups = (group_ir_14)
    ikta = Institute(UniversityName.LPNU,"IKTA",ikta_groups)
if __name__ == "__main__":
    main()
