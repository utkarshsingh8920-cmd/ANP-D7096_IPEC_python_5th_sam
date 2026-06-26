"""----------------Problem Statement---------------------------------
A student appears in 5 subjects. 
Rules: 
• Minimum 40 marks in every subject to pass.  
• Distinction → Average ≥ 75  
• First Division→ Average ≥ 60  
• Second Division → Average ≥ 50  
• Pass  → Average ≥ 40  
• Fail if any subject score < 40 
---------------------------------------------------------------------- 
Sample Input 
Hindi : 85 
English : 78 
Mathematics : 82 
Science : 75 
Computer : 90 
----------------------------------------------------------------------
Sample Output 
Average Marks: 82.0 
Result: PASS 
Classification: Distinction 
---------------------------------------------------------------------
"""
#----------------------------Coding---------------------------------
# Online Examination Result Analyzer
print("-------------------------------------------")
hindi = int(input("Enter marks of student in Hindi: "))
english = int(input("Enter marks of student in English: "))
math = int(input("Enter marks of student in Mathematics: "))
science = int(input("Enter marks of student in Science: "))
computer = int(input("Enter marks of student in Computer: "))
print("-------------------------------------------")

# Validation
if (hindi < 0 or hindi > 100 or
    english < 0 or english > 100 or
    math < 0 or math > 100 or
    science < 0 or science > 100 or
    computer < 0 or computer > 100):

    print("Invalid Marks")

else:

    average = (hindi + english + math + science + computer) / 5

    print("Average Marks:", average)

    if (hindi < 40 or english < 40 or math < 40 or
        science < 40 or computer < 40):

        print("Result: FAIL")

    else:

        print("Result: PASS")

        if average >= 75:
            print("Classification: Distinction")

        elif average >= 60:
            print("Classification: First Division")

        elif average >= 50:
            print("Classification: Second Division")

        else:
            print("Classification: Pass")
    print("-------------------------------------------")
"""
Output:
-------------------------------------------
Enter marks of student in Hindi: 56
Enter marks of student in English: 56
Enter marks of student in Mathematics: 45 
Enter marks of student in Science: 45
Enter marks of student in Computer: 54
-------------------------------------------
Average Marks: 51.2
Result: PASS
Classification: Second Division"""