class Employee:
    base_salary = 1200

    def __init__(self, role, pay_factor):
        self.role = role
        self.pay_factor = pay_factor
        self.salary = self.base_salary

    def calc_salary(self):
        return self.salary * self.pay_factor

    def add_raise(self, raise_):
        self.salary += raise_

    def printEmployee(self):
        print(
            "role:",
            self.role,
            "salary:",
            self.calc_salary(),
            "role_pay_factor:",
            self.pay_factor,
        )


class Manager(Employee):
    def __init__(self):
        super().__init__("manager", 4.5)

    def sanctionEmployee(self, employee, amount):
        if isinstance(employee, Employee) and type(employee) != Manager:
            employee.add_raise(-amount)


class Engineer(Employee):
    def __init__(self):
        super().__init__("engineer", 3.0)


class Salesperson(Employee):
    def __init__(self):
        super().__init__("salesperson", 2.0)

    def cry(self):
        print("I need a raise")


employees = [Salesperson(), Engineer(), Manager()]
for e in employees:
    e.printEmployee()

employees[0].cry()

employees[2].sanctionEmployee(employees[0], 300)
for e in employees:
    e.printEmployee()
