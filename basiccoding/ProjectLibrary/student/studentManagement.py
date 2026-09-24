class StudentManagement:
    def __init__(self):
        self.studentlist=[]

    def add_student(self,sname):
        self.studentlist.append(sname)

    def listofstudents(self):
        return self.studentlist
        