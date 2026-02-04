'''
BSCIT-05-0133/2024
Masindano Masila
'''
#Decision Making

#prompting the user to enter the salary
salary = float(input("Enter the salary: "))

#prompting the user to enter years of service
YearsOfService = int(input("Enter the years of service: "))

#decision making using if..elif statement
if(YearsOfService > 10):
    bonus = 0.1 * salary
elif(YearsOfService >= 6 and YearsOfService <= 10):
    bonus = 0.8 * salary
else:
    bonus = 0.6 * salary

print("The bonus is: ", bonus)
f = open("C:\\Users\\hp\\OneDrive\\Documents\\Desktop\\python files\\bonus.txt","w")
print("The bonus is: ",bonus, file=f)
f.close()
    
    


