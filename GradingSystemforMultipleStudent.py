'''
BSCIT-05-0133/2024
Masindano Masila
'''

# Function to determine grade based on marks
def grade_student(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Function to take a list of marks and return grades
def grade_list(marks):
    grades = []
    for mark in marks:
        grades.append(grade_student(mark))
    return grades

# Main program
# Ask user to input marks separated by space
marks_input = input("Enter the marks of students separated by space: ")
marks = [int(x) for x in marks_input.split()]

# Get grades
grades = grade_list(marks)

# Print results
for i in range(len(marks)):
    print(f"Mark: {marks[i]}, Grade: {grades[i]}")
