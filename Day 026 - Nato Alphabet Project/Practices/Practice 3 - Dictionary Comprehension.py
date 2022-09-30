from random import randint
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {name:randint(0,100) for name in names}

print(student_scores)

# Chop down a Dictionary
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}

print(passed_students)

#Chop a Dictionary to a List
passed_students2 = [name for (name, score) in student_scores.items() if score > 60]
print(passed_students2)
