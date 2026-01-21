'''
Masindano Masila
BSCIT-05-0133/2024
'''

#prompting the user to enter the input
hours_worked= float(input("Enter The hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))

#calculating
Gross_pay = hours_worked * rate_per_hour

#printing the gross pay
print("Gross Pay: ", Gross_pay)

#printing to the file
f = open("C:\\Users\\hp\\OneDrive\\Documents\\Desktop\\python files\\python.txt", "a") #w-write, r-read, a-append
print("Gross Pay: ", Gross_pay, file=f)
f.close()

#reading the radius 
radius = 2
PI = 3.142

#calculating the volume
volume = 4/3 * PI * radius * radius * radius

#printing to screen
print("The volume is: ", volume)

#printing to file
f = open("C:\\Users\\hp\\OneDrive\\Documents\\Desktop\\python files\\python.txt", "a") #w-write, r-read, a-append
print("The volume is: ", volume, file=f)
f.close()

