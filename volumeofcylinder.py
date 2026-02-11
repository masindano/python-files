'''
BSCIT-05-0133/2024
Masindano Masila
'''

#volume, radius, height

#import math
import math

#creating the function
def volumeOfCylinder(radius, height):
    volume = math.pi * radius * radius * height
    return volume


#prompt the user to enter radius and height
radius = int(input("Enter the radius: "))
height = float(input("Enter the height of the cylinder: "))

#function call and storing result
result = volumeOfCylinder(radius, height)

#printing the result 
print(f"Volume is: {result}")

             
