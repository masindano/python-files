'''
Masindano Masila
BSCIT-05-0133/2024
'''
#python variables

#Assigning variables 
name = "John"
age = 20
discount = 20.35
tall = True
x,y,z = "Orange", 10, 3.142
a=b=c="James"
a=10
b=20
sum = a + b

#Different ways of printing the output
print(sum) #output 30
print("The sum is ", sum) #The sum is 30
print(f"The sum is{sum:.2f} and age is {age}")
f = open("C:\\Users\\hp\\OneDrive\\Documents\\Desktop\\python files\\python.txt", "w") #w-write, r-read, a-append
print("The sum is: ",sum, file=f)
print("Name:",name, "\n""Sum: ", sum, file=f)
f.close()

#prompting the user to enter the input
last_name= input ("Enter your name: ")
score = int(input("Enter marks: "))
budget = float(input("Enter budget: "))

#displaying on screen
print("The last name is: ", last_name)
print("The score is: ", score)
print("The budget is: ", budget)

#printing all in one line
print(f"The name is {last_name} ,score is {score} and budget is {budget}")

#displaying in a file
f = open("C:\\Users\\hp\\OneDrive\\Documents\\Desktop\\python files\\python.txt", "a") #w-write, r-read, a-append
print("The last name is: ", last_name, file=f)
print("The score is: ", score, file=f)
print("The budget is: ", budget, file=f)
f.close()
