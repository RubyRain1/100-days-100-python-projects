import random
#dictionary comprehension

# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()} creates new dict based on existing dict.
#new_dict = {new_key:new_value for (key,value) in dict.items() if test} same just with if test.

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']

student_scores = {student:random.randint(1,100) for student in names}


passed_students = {student:score for (student,score) in student_scores.items() if score > 50}
print(passed_students)