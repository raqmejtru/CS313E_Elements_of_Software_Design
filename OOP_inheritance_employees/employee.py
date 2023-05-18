#  File: employee.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 02/10/2023
#  Date Last Modified: 02/11/2023


# Parent: Employee
class Employee:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')

    def __str__(self):
        return f'{self.name}, {self.id}, {self.salary}'


# Child 1/3 of employee: Permanent employee
class PermanentEmployee(Employee):

    # Inherit employee properties, plus benefits
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits')

    # Calculate salary based on selected benefits
    def cal_salary(self):
        if self.benefits == ['health_insurance']:
            return float(self.salary) * 0.9
        elif self.benefits == ['retirement']:
            return float(self.salary) * 0.8
        elif self.benefits == ['retirement', 'health_insurance']:
            return float(self.salary) * 0.7

    def __str__(self):
        return f'{self.name}, {self.id}, {self.salary}, {self.benefits}'


# Child 2/3 of employee: Manager
class Manager(Employee):

    # Inherit employee properties, plus bonus
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus')

    # Calculate salary based on additional bonus
    def cal_salary(self):
        return float(self.salary) + float(self.bonus)

    def __str__(self):
        return f'{self.name}, {self.id}, {self.salary}, {self.bonus}'


# Child 3/3 of employee: Temporary Employee
class TemporaryEmployee(Employee):

    # Inherit employee properties, plus hours
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours')

    # Output represents hours worked * hourly pay (i.e., `salary`)
    def cal_salary(self):
        return float(self.salary) * float(self.hours)

    def __str__(self):
        return f'{self.name}, {self.id}, {self.salary}, {self.hours}'


# Child 1/1 of temporary employee: Consultant
class Consultant(TemporaryEmployee):

    # Inherit temporary employee properties, plus travel
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get('travel')  # number of trips

    # Calculate salary, including $1,000 per trip
    def cal_salary(self):
        return TemporaryEmployee.cal_salary(self) + float(self.travel) * 1000

    def __str__(self):
        return f'{self.name}, {self.id}, {self.salary}, {self.hours}, {self.travel}'


# Child of manager and consultant: Consultant Manager
class ConsultantManager(Manager, Consultant):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Consultant.__init__(self, **kwargs)

    # Calculates salary similar to a consultant, plus a bonus
    def cal_salary(self):
        return Consultant.cal_salary(self) + float(self.bonus)

    def __str__(self):
        return f'{self.name}, {self.id}, {self.salary}, {self.hours}, {self.travel}, {self.bonus}'


def main():
    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", id="UT3", salary=100, hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:", matt.cal_salary(), "\n")


if __name__ == "__main__":
    main()
