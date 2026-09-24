from student import Student
from studentManagement import StudentManagement

class SchoolTest:
    schoolstudents = StudentManagement()

    newstudent = Student("101", "Shourya")
    schoolstudents.add_student(newstudent)

    abc = schoolstudents.listofstudents()
    print(abc)
    
   

    