"""Program to store names and marks of 50 students
and display eligible students (marks > 75)"""

names = []
marks = []

for i in range(10):
    name = input("Enter name of student  ")

    mark = int(input("Enter marks of "))

    # Validation
    if mark < 0 or mark > 100:
        print("Invalid marks! Setting marks to 0.")
        mark = 0

    names.append(name)
    marks.append(mark)

# Display eligible students
print("\n------ Eligible Students ------")

for i in range(10):
    if marks[i] > 75:
        print(names[i], "is eligible for admission with marks:", marks[i])
#------------------------------------------------------------------------
"""
Output :
Enter marks of 4 
Enter name of student  bhat
Enter marks of 445
Invalid marks! Setting marks to 0.
Enter name of student  fh
Enter marks of 34
Enter name of student  fgh
Enter marks of 56
Enter name of student  gfhtf
Enter marks of 546
Invalid marks! Setting marks to 0.
Enter name of student  fyf
Enter marks of 46
Enter name of student  hgf
Enter marks of 56
Enter name of student  hf
Enter marks of 56
Enter name of student  gh
Enter marks of 78
Enter name of student  ghj
Enter marks of 90 

------ Eligible Students ------
gh is eligible for admission with marks: 78
ghj is eligible for admission with marks: 90
"""