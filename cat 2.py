# i. Prompt the user to enter marks for 2 subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))

# ii. Find the average of the marks
average = (subject1 + subject2) / 2
print("Average marks:", average)

# iii. Use elif condition to decide the grade
if 70 <= average <= 100:
    grade = "A"
elif 60 <= average <= 69:
    grade = "B"
elif 50 <= average <= 59:
    grade = "C"
elif 40 <= average <= 49:
    grade = "D"
elif average < 40:
    grade = "E (Fail)"
else:
    grade = "Invalid score"

print("Grade:", grade)
