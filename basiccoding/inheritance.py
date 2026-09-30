class Developer:

    def write_code(self):
        print("Writing code")


class Tester(Developer):

    def test_code(self):
        print("Testing code")
emp1 = Tester()
emp1.write_code()
emp1.test_code()

class Employee(Tester):

    def work(self):
        print("Employee is working")


emp = Employee()

# emp.write_code()
emp.test_code()
emp.work()