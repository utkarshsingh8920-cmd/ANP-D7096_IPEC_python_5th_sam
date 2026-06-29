"""
-----------------------------------------Problem Statement------------------------------------------------- 
A company has N employees. 
Accept the salary of each employee and determine: 
• Highest salary  
• Lowest salary  
• Average salary  
• Number of employees earning more than ₹50,000 
-------------------------------------------------------------
 """
#----------------------------------------------------------------------
#------------------------------------------Coding Section-----------------------------------------
#User can enter number of employees
n = int(input("Enter Number of Employees: "))

total = 0
count = 0

for i in range(1, n + 1):

    salary = float(input("Enter Salary: "))

    total += salary

    if i == 1:
        highest = lowest = salary
    else:
        if salary > highest:
            highest = salary
        if salary < lowest:
            lowest = salary

    if salary > 50000:
        count += 1

print("Highest Salary =", highest)
print("Lowest Salary =", lowest)
print("Average Salary =", total / n)
print("Employees earning above ₹50,000 =", count)
#--------------------------------------------------------
"""
Output :
Enter Number of Employees: 5
Enter Salary: 200000
Enter Salary: 600000
Enter Salary: 770000 
Enter Salary: 566546 
Enter Salary: 343009 
Highest Salary = 770000.0
Lowest Salary = 200000.0
Average Salary = 495911.0
Employees earning above ₹50,000 = 5
"""
