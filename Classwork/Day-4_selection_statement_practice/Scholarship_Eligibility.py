"""Problem Statement 
A university provides a scholarship only to students who score 90 or above. 
Write a Python program to accept a student's percentage and determine whether the student is eligible. 
• If percentage is 90 or above, display: 
Scholarship Approved 
• Otherwise display: 
Scholarship Not Approved 
------------------------------------------------------------------
Sample Input 
92 
-------------------------------------------------------------------
Sample Output 
Scholarship Approved """
#-------------------------Coding------------------------------------
# University Scholarship Eligibility Program
print("---------------------------------------------------------")
percentage = float(input("Enter the student's percentage: "))

if percentage<0 or 100<percentage:
    exit("Percentage can not be negative and more then 100")

if percentage >= 90:
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")


print("---------------------------------------------------------")
"""Output :
---------------------------------------------------------
Enter the student's percentage: 99
Scholarship Approved
---------------------------------------------------------
"""


