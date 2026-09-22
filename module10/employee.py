class Human:

    def __init__(self):
        self.is_human = True
        self.existential_crisis = True

    def print_number_of_legs(self):
        print("2 legs")

class Employee(Human):

    total_employees = 0

    def __init__(self, first_name, last_name):
        # Employee.total_employees = Employee.total_employees + 1
        Employee.total_employees += 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}, crisis: {self.existential_crisis}")

        self.print_number_of_legs()

employees = []
employees.append(Employee("Viivi", "Virta"))
employees.append(Employee("Ahmed", "Habib"))

for e in employees:
    e.print_information()
    e.print_number_of_legs()
