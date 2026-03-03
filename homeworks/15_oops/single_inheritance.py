class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_employee_info(self):
        return (f"Employee Name: {self.name}, Employee Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name,salary)
        self.dept = dept

    def get_manager_info(self):
        return (f"Manager Info:{self.name}, Manager Salary: {self.salary}, Manager Department: {self.dept}")

if __name__ == '__main__':
    emp = Employee("Ajay", 20000)
    mgr = Manager("Logi", 200000, "SW & ADAS")
    print(emp.get_employee_info())
    print(mgr.get_employee_info())
    print(mgr.get_manager_info())