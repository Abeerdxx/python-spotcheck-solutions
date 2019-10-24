the_file = open("attendance.txt")
names = the_file.read().split("\n")

student_attendance = {}

for name in names:
    if name in student_attendance:
        student_attendance[name] += 1
    else:
        student_attendance[name] = 1

print(student_attendance)
