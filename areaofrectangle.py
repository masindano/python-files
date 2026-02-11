'''
BSCIT-05-0133/2024
Masindano Masila
'''
# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area

# Prompt the user to enter length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and store the result
area = area_of_rectangle(length, width)

# Print the result
print(f"The area of the rectangle is: {area}")
