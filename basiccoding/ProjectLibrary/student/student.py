class Student:
    def __init__(self,rollno,sname):
        self.rollno = rollno
        self.sname = sname

    def displaystudents(self):
        return self.rollno+self.sname

    def __rep__(self):
        return self.rollno + " " + self.sname