'''
BSCIT-05-0133/2024
Masindano masila
'''
# simpleInterest function
def simpleInterest(principal, rate, time):
    interest = principal * rate * time / 100
    return interest

# prompt the user to enter the principal, rate and time
principal = float(input("Enter the principal Amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

# function call and store result
result = simpleInterest(principal, rate, time)

# print result
print(f"The Interest is: {result}")
