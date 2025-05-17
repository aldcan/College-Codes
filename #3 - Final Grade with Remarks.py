# Student Final Grade Calculator 
# November 28, 2023
# Aldrian P. Cabaccan
# This program will compute the final grade of num1student with Lecture and Laboratory scores.

# Creates num1function that holds the input prompt and takes in the grade component.
def grades(component):
# Holds the input prompt
    grade = float(input(f"Enter lecture {component} of the student: "))
    return grade

# Assigns the corresponding component to the input prompt. 
lecture = grades("lecture")
laboratory = grades("laboratory")

# Calculates the final grade based on the given formula.
final_grade =(lecture * 0.7) + (laboratory * 0.3)

# Grade condition for the corresponding remark.
remarks = "Passed" if final_grade >= 75 else "Failed"

# Displays the computed grade with the corresponding remark.
print (f'The final grade of the student is {final_grade:.2f}')
print (f"Remarks: {remarks}")

