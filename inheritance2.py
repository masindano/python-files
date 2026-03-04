"""
Program Title: Multilevel Inheritance Demonstration
Author: Masindano Masila
Reg No: BSCIT-05-0133/2024
Description:
    This program illustrates multilevel inheritance in Python.
    A Puppy inherits from Dog, and Dog inherits from Animal.
    Each class contains its own constructor and behavior methods.
"""

# Base Class: Animal
class Animal:
    def __init__(self):
        """
        Constructor for Animal class.
        Executes when an Animal (or derived class) object is created.
        """
        print("Animal constructor initialized.")

    def fur(self):
        """
        Displays a general characteristic of animals.
        """
        print("I have fur all over my body.")


# Derived Class: Dog
# Inherits from Animal
class Dog(Animal):
    def __init__(self):
        """
        Constructor for Dog class.
        Calls the parent (Animal) constructor first.
        """
        super().__init__()
        print("Dog constructor initialized.")

    def bark(self):
        """
        Displays barking behavior.
        """
        print("Dog barking.")


# Derived Class: Puppy
# Inherits from Dog
class Puppy(Dog):
    def __init__(self, name):
        """
        Constructor for Puppy class.
        Calls the Dog constructor and assigns a name.
        """
        super().__init__()
        self.name = name
        print("Puppy constructor initialized.")

    def play(self):
        """
        Displays playful behavior of the puppy.
        """
        print(f"{self.name} plays all the time.")


# Main Program Execution
if __name__ == "__main__":
    # Creating an instance of Puppy
    bosco = Puppy("Bosco")

    print("\n--- Calling Methods ---")
    
    # Calling methods from different inheritance levels
    bosco.play()   # Method from Puppy
    bosco.bark()   # Method from Dog
    bosco.fur()    # Method from Animal
