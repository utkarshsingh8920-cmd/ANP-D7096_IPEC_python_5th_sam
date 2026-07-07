"""
Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0-100) as a parameter.  
• Return the grade according to the following criteria:  
o 90 and above → A+  
o 75-89 → A  
o 60-74 → B  
o 40-59 → C  
o Below 40 → Fail 
The main program should: 
• Accept marks of 5 students.  
• Call the function for each student.  
• Display the marks and corresponding grade.  
"""
def grade_calculater(marks):
    if marks>=90:
        return "A+"
    elif  marks>=75:
        return "A"
    elif marks>=60:
        return "B"
    elif marks>=40:
        return "c"
    else:
        return "Fail"
    
#main program
for x in range(5):
    marks = int(input("Enter marks of student :" ))

    if marks <0 and marks>100:
       exit("Enter correct marks")
    print ("Grade of student is ",grade_calculater(marks))

"""
Enter marks of student :23
Grade of student is  Fail
Enter marks of student :78
Grade of student is  A
Enter marks of student :90 
Grade of student is  A+
Enter marks of student :57
Grade of student is  c
Enter marks of student :56
Grade of student is  c
"""