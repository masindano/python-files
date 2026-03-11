
# Importing required module for creating abstract classes
from abc import ABC, abstractmethod


# Abstract Base Class: Employee
# This class represents a general employee.
# It contains private attributes and an abstract method
# that must be implemented by subclasses.

class Employee(ABC):

    # Constructor to initialize employee details
    def __init__(self, name, salary):
        self.__name = name        # private attribute (encapsulation)
        self.__salary = salary    # private attribute

    # Method to display employee information
    def display_info(self):
        print("Employee Name:", self.__name)

    # Getter method to access the private salary attribute
    def get_salary(self):
        return self.__salary

    # Abstract method that will be implemented differently
    # in the child classes
    @abstractmethod
    def calculate_salary(self):
        pass


# Child Class: FullTimeEmployee
# Inherits from the Employee class
# Implements its own version of calculate_salary()

class FullTimeEmployee(Employee):

    def calculate_salary(self):
        # Full-time employees receive the full salary
        return self.get_salary()


# Child Class: PartTimeEmployee
# Also inherits from the Employee class
# Implements salary calculation differently

class PartTimeEmployee(Employee):

    def calculate_salary(self):
        # Part-time employees receive half of the salary
        return self.get_salary() * 0.5


# Main Program
# Creating employee objects and demonstrating polymorphism

# Creating objects for different types of employees
employee1 = FullTimeEmployee("Maxii", 5000)
employee2 = PartTimeEmployee("Raven", 4000)

# Storing the objects inside a list
employees = [employee1, employee2]

# Loop through the list and display employee details
for emp in employees:
    emp.display_info()                           # show employee name
    print("Calculated Salary:", emp.calculate_salary())  # polymorphic behavior
    print("-" * 30)
