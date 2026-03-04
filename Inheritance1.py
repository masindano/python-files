'''
Masindano Masila
BSCIT-05-0133/2024
'''

#inheritance Example
from abc import ABC, abstractmethod
# Create Employee class
class Employee(ABC):
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
     #method overriding   
    @abstractmethod
    def calculate_salary(self):
        pass   


# Subclass 1
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, salary, hourly_rate, hours_worked):
        super().__init__(emp_id, name, salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        sal = self.hourly_rate * self.hours_worked
        return sal


# Subclass 2
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, salary, monthly_salary):
        super().__init__(emp_id, name,salary)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        self.salary = self.monthly_salary
        return self.salary
    
#creating the objects
emp1 = HourlyEmployee(100, "Maxii", 30000, 1000, 24)
sal = emp1.calculate_salary()
print("Salary for Maxii is: ", sal)
emp2 = SalariedEmployee(101, "Raven", 100000, 200000)
sal = emp2.calculate_salary()
print("salary for raven is: ", sal)
