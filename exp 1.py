print('**** Welcome to the LAB grade calculator! ****')
print()
name = input('Who are we calculating grades for? ==> ')
print()
Labs_grade = float(input("Enter the Labs grade? ==> "))
if Labs_grade > 100:
    print("The lab value should have been 100 or less. It has been changed to 100.")
    Labs_grade = 100
elif Labs_grade < 0:
    print("The lab value should have been zero or greater. It has been changed to zero.")
    Labs_grade = 0
print(Labs_grade)
print()
EXAMS_grade = float(input('Enter the EXAMS grade? ==> '))
if EXAMS_grade < 0:
    print("The exam value should have been zero or greater. It has been changed to zero.")
    EXAMS_grade = 0
elif EXAMS_grade > 100:
    print("The EXAMS grade should have been 100 or less. It has been changed to 100.")
    EXAMS_grade = 100
print(EXAMS_grade)
print()
Attendance_grade = float(input('Enter the Attendance grade? ==> '))
if Attendance_grade < 0:
    print("The Attendance grade should have been zero or greater. It has changed to zero.")
    Attendance_grade = 0
elif Attendance_grade > 100:
    print("The Attendance grade should have been 100 or less. It has been changed to 100.")
    Attendance_grade = 100
print(Attendance_grade)
print()

Labs_grade = (Labs_grade * 0.7)
EXAMS_grade = (EXAMS_grade * 0.2)
Attendance_grade = (Attendance_grade * 0.1)

final_grade = (Labs_grade + EXAMS_grade + Attendance_grade)
print('The weighted grade for ', name, ' is ', final_grade,)

if final_grade >= 90 and final_grade <= 100:
   print(name, 'has a letter grade of A')
elif final_grade >= 80 and final_grade <90:
    print(name, 'has a letter grade of B')
elif final_grade >= 70 and final_grade <80:
    print(name, 'has a letter grade of C')
elif final_grade >= 60 and final_grade <70:
    print(name, 'has a letter grsde of D')
elif final_grade >=0 and final_grade <60:
    print(name, 'has a letter grade of F')
print()
print('**** Thanks for using the Lab grade calculator ****')
