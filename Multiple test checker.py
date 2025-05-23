def grade_question(student_answers, answer_key, question_number):
    return True if student_answers[question_number] == answer_key[question_number] else False
    

def calculate_score(student_answers, answer_key):
    score = 0
    for i, value in enumerate(student_answers):
        if grade_question(student_answers, answer_key, i) == True:
            score += 1
    return score

