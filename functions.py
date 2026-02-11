'''
BSCIT-05-0133/2024
Masindano Masila
'''

#python Functions
while True:
        def sum(a, b):
            sum = a + b
            return sum
        #function call
        a = sum(10, 20)
        print(a)



        def myName(name, age):
            print("My name is " +name+ "and I am" +str(age)+" years old")
            print(f"My name is {name} and I am {age} years old")

        #promt the user to enter the name and the age
        f_name = input("Enter the user name: ")
        years = int(input("Enter the age: "))

        myName(f_name, years)
