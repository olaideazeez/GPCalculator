# GP Calculator
# Salako Abdulazeez
# 08169292596

print('''
Please go through the instructions below:
1. Number of courses: meaning how many course offered
2. Grade: meaning the grade scored in each of the courses offered
          e.g on a scale of 4 point we have(A1,A2,B1,B2,C1,C2,D1,D2,F)
          and on a scale of 5 point we have(A,B,C,D,E,F)
3. Unit: meaning the course unit of the grade entered
4. Ensure you use upper case for grade entered in order not to encounter an error
''')


num_of_courses = int(input("Enter number of courses:"))
x = 0
grade_unit = {}

# Get input for users
while x < num_of_courses:
    grade = input("Enter grade:")
    unit = input("Enter course unit:")
    validGrade = ("A", "B", "C", "D", "E", "F", "A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2")
    validUnit = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    # check if input is valid
    if (grade not in validGrade) and (unit not in validUnit):
        print("Enter valid input")
        num_of_courses = num_of_courses + 1
    else:
        # set grade and unit as key value pairs
        grade_unit.setdefault(grade, []).append(unit)
    x = x + 1

# Get the point equivalent of the grade
def assign_grade_point(letter_grade):
    if(letter_grade == "A1"):
        return 4.00
    elif (letter_grade == "A2"):
        return 3.50
    elif (letter_grade == "B1"):
        return 3.25
    elif (letter_grade == "B2"):
        return 3.00
    elif (letter_grade == "C1"):
        return 2.75
    elif (letter_grade == "C2"):
        return 2.50
    elif (letter_grade == "D1"):
        return 2.25
    elif (letter_grade == "D2"):
        return 2.00
    elif (letter_grade == "F"):
        return 0.00
    elif (letter_grade == "A"):
        return 5.00
    elif (letter_grade == "B"):
        return 4.00
    elif (letter_grade == "C"):
        return 3.00
    elif (letter_grade == "D"):
        return 2.00
    elif (letter_grade == "E"):
        return 1.00

def calculateGP():
    CGP = 0
    total_unit = 0
    for grade,units in grade_unit.items():
            for unit in units:
                gradePoint = assign_grade_point(grade)
                unit = float(unit)
                IGP = gradePoint * unit
                total_unit = total_unit + unit
                CGP = CGP + IGP
    GP = CGP/total_unit
    print("Your GP as calculated is ", GP)

calculateGP()

