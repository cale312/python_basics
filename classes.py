class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayEmployee(self):
        print("Name: {}, Salary: {}".format(self.name, self.salary))

emp1 = Employee("Cale", 4000)
emp2 = Employee("Oasin", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee count: {}".format(Employee.empCount))
