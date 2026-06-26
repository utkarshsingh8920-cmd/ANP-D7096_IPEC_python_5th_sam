"""Problem Statement 3 : Student Grade Calculator
A school assigns grades based on the marks obtained by students according to the following criteria:
* Marks 90 and above → Grade A
* Marks 75 to 89 → Grade B
* Marks 50 to 74 → Grade C
* Below 50 → Grade F
Write a Python program to accept marks from the user and display the corresponding grade.
Sample Input
Enter Marks: 92
Sample Output
Grade A
Sample Input
Enter Marks: 80
Sample Output
Grade B
Sample Input
Enter Marks: 65
Sample Output
Grade C
Sample Input
Enter Marks: 35
Sample Output
Grade F"""
#---------------------------Codeing---------------------------
"""Student Grade Calculator"""

marks = float(input("Enter student Marks : "))
# Validate marks
if marks < 0 or marks > 100:
    print("Error: Marks should be between 0 and 100.")
# if student get grater then 90 student obtain grade A
elif marks >= 90:
    print("-----------------------------------")
    print("Student obtain Grade A")
    print("-----------------------------------")
elif marks >= 75:
    print("-----------------------------------")
    print("Student obtain Grade B")
    print("-----------------------------------")
elif marks >= 50:
    print("-----------------------------------")
    print("Student obtain Grade C")
    print("-----------------------------------")
else:
    print("-----------------------------------")
    print("Student obtain Grade F")
    print("-----------------------------------")
"""Output :
Enter student Marks : 43
Student obtain Grade F
"""
