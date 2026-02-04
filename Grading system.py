'''
BSCIT-05-0133/2024
Masindano Masila
'''
# Decision Making Program
while True:
        # prompt the user to enter the marks of 3 subjects
        subject1 = int(input("Enter the marks of the first subject: "))
        subject2 = int(input("Enter the marks of the second subject: "))
        subject3 = int(input("Enter the marks of the third subject: "))

        # check if marks are valid
        if (subject1 < 0 or subject1 > 100 or
            subject2 < 0 or subject2 > 100 or
            subject3 < 0 or subject3 > 100):

            print("Invalid marks entered. Marks must be between 0 and 100.")

        else:
            # compute total and average marks
            total_marks = subject1 + subject2 + subject3
            average_score = total_marks / 3

            # determine the grade
            if 70 <= average_score <= 100:
                grade = "A"
            elif 60 <= average_score < 70:
                grade = "B"
            elif 50 <= average_score < 60:
                grade = "C"
            elif 40 <= average_score < 50:
                grade = "D"
            else:
                grade = "Fail"

            # print output on the screen
            print("Average Score:", average_score)
            print("Grade:", grade)

            # save output to a file
            file = open("results.txt", "w")
            file.write("Student: Masindano Masila\n")
            file.write("Registration: BSCIT-05-0133/2024\n")
            file.write("Average Score: " + str(average_score) + "\n")
            file.write("Grade: " + grade)
            file.close()

