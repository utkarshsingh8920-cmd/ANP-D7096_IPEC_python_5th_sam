"""-------------------------Problem Statement-----------------------
An employee is evaluated using: 
• Project Score  
• Attendance Percentage  
• Client Feedback Score  
Rules: 
• Excellent → All scores above 90  
• Good → Scores above 75  
• Average → Scores above 60  
• Poor → Otherwise  
Additional Rule: 
• Attendance below 70% cannot receive more than Average rating.  
---------------------------------------------------------------------
Sample Input 
Project Score: 95 
Attendance: 65 
Client Feedback: 92 
Sample Output 
Performance Rating: Average 
Reason: Attendance below 70%
-----------------------------------------------------------------------
"""
#---------------------Codeing----------------------------------------
# Employee Performance Evaluation
# Take input from the user
print("--------------------------------------------------")
project = int(input("Enter Project Score: "))
attendance = int(input("Enter Attendance Percentage: "))
feedback = int(input("Enter Client Feedback Score: "))
print("--------------------------------------------------")

# Validate input
if (project < 0 or project > 100 or
    attendance < 0 or attendance > 100 or
    feedback < 0 or feedback > 100):
    print("_________________________________________________")
    print("Invalid Input! Enter values between 0 and 100.")
    print("_________________________________________________")

else:

    # Attendance below 70 cannot get above Average
    if attendance < 70:
        print("_________________________________________________")
        print("Performance Rating: Average")
        print("Reason: Attendance below 70%")
        print("_________________________________________________")

    # Excellent
    elif project > 90 and attendance > 90 and feedback > 90:
        print("_________________________________________________")
        print("Performance Rating: Excellent")
        print("_________________________________________________")

    # Good
    elif project > 75 and attendance > 75 and feedback > 75:
        print("_________________________________________________")
        print("Performance Rating: Good")
        print("_________________________________________________")

    # Average
    elif project > 60 and attendance > 60 and feedback > 60:
        print("_________________________________________________")
        print("Performance Rating: Average")
        print("_________________________________________________")

    # Poor
    else:
        print("_________________________________________________")
        print("Performance Rating: Poor")
        print("_________________________________________________")
"""Output:
--------------------------------------------------
Enter Project Score: 96
Enter Attendance Percentage: 78
Enter Client Feedback Score: 88
--------------------------------------------------
_________________________________________________
Performance Rating: Good
_________________________________________________
"""