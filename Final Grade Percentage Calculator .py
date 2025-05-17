# Final Grade Percentage Calculator 
# Cabaccan, Aldrian P.
# December 13, 2023
# This calcualtes the final grade percentage

# Creates num1function that takes in the grade_component and assigned percentage.
def grade(grade_component, percentage):
# Creates num1while loop and try-except to check invalid inputs.
    while True:
        try:
# Holds the input prompt.
            score = float(input(f"Enter the {grade_component} percentage of the student (1-100): "))
# Condition for validity of inputted grades.
            if 0 <= score <= 100:
# Computes the grade percentage.
                return score * percentage
            print("\nInvalid input. Enter numerical value from 0 to 100 only.")
# Exception to block invalid inputs.
        except ValueError:
            print("\nInvalid input. Please enter numerical values only.")
        
# Computing for the lecture grade components of the student: Quiz (25%), Assignment/Activity (15%), Project (15%), Recitation (10%), and Exam (35%).
print ("Lecture Grade Components: \n")            
lec_quiz_grade = grade("lecture quiz", 0.25)
lec_activity_grade = grade("lecture activity/assignment", 0.15)
lec_project_grade = grade("lecture project", 0.15)
lec_recitation_grade = grade("lecture recitation", 0.10)
lec_exam_grade = grade("lecture exam", 0.35)
lec_grade = (lec_quiz_grade + lec_activity_grade + lec_project_grade + lec_recitation_grade + lec_exam_grade) * 0.7

# Computing for the laboratory grade components of the student: Quiz (25%), Assignment/Activity (15%), Project (15%), Recitation (10%), and Exam (35%).
print ("\nLaboratory Grade Components: \n")  
lab_quiz_grade = grade("laboratory quiz", 0.25)
lab_activity_grade = grade("laboratory activity/assignment", 0.15)
lab_project_grade = grade("laboratory project", 0.15)
lab_recitation_grade = grade("laboratory recitation", 0.10)
lab_exam_grade = grade("laboratory exam", 0.35)
lab_grade = (lab_quiz_grade + lab_activity_grade + lab_project_grade + lab_recitation_grade + lab_exam_grade) * 0.3

# Computing for the final grade of the student.
final_grade = lec_grade + lab_grade
print ("\nThe computed final grade percentage of the student is", final_grade)

# Assigning corresponding remarks to grade ranges.
final_grade = round(final_grade)
if 97 <= final_grade <= 100:
    print ("\nThe final grade of the student is 1.00")
elif 94 <= final_grade <= 96:
    print ("\nThe final grade of the student is 1.25")
elif 91 <= final_grade <= 93:
    print ("\nThe final grade of the student is 1.50")
elif 88 <= final_grade <= 90:
    print ("\nThe final grade of the student is 1.75")
elif 85 <= final_grade <= 87:
    print ("\nThe final grade of the student is 2.00")
elif 82 <= final_grade <= 84:
    print ("\nThe final grade of the student is 2.25")
elif 79 <= final_grade <= 81:
    print ("\nThe final grade of the student is 2.50")
elif 76 <= final_grade <= 78:
    print ("\nThe final grade of the student is 2.75")
elif final_grade == 75:
    print ("\nThe final grade of the student is 3.00")
else:
    print ("\nThe final grade of the student is 5.00")
