# Day 5.1 Average Height Exercise

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_height = 0
num_students = 0
for height in student_heights:
    sum_height += height
    num_students += 1
average = round(sum_height / num_students)

print(average)