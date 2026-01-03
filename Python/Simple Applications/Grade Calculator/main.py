from Grades import Grades
midterm = eval(input("Midterm grade: "))
final = eval(input("Final Grade: "))
quiz = eval(input("Quiz grade: "))
lab = eval(input("Lab Grade:  "))

grades = Grade(midterm, final, quiz, lab)
student = Grades.grades_weight()
print(student)
