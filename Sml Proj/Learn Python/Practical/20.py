#Program 20
n = int(input("Enter the number of students: "))
students = {}
for i in range(n):
    roll = input("Enter the roll number of student {}: ".format(i+1))
    name = input("Enter the name of student {}: ".format(i+1))
    marks = int(input("Enter the marks of student {}: ".format(i+1)))
    students[roll] = {"name": name, "marks": marks}
    print('')
print("List of students who have marks above 75:")
for student in students.values():
    if student["marks"] > 75:
        print(student["name"])
