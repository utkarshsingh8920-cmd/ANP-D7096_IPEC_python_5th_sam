"""------------------------Problem Statement------------------------
Assign access levels based on: 
Roles: 
• Admin  
• Manager  
• Employee  
• Guest  
Conditions: 
• Admin + Security Clearance ≥ 5 → Full Access  
• Manager + Experience > 5 Years → Department Access  
• Employee + Experience > 2 Years → Limited Access  
• Guest → Read-Only Access  
• Inactive Account → No Access 
--------------------------------------------------------------------- 
Sample Input 
Role: Admin 
Security Clearance: 6 
Account Status: Active
--------------------------------------------------------------------- 
Sample Output 
Access Level: FULL ACCESS 
---------------------------------------------------------------------
"""
# Online Examination Result Analyzer
#-------------------------Coding-----------------------------------
# Multi-Level Access Control System
print("-------------------------------------------------------")
role = input("Enter Role: ")
status = input("Account Status (Active/Inactive): ")
print("-------------------------------------------------------")

# Check Account Status
if status == "Inactive" or status == "inactive":
    print("Access Level: NO ACCESS")

else:

    if role == "Admin" or role == "admin":

        clearance = int(input("Enter Security Clearance: "))

        if clearance >= 5:
            print("Access Level: FULL ACCESS")
        else:
            print("Access Denied")

    elif role == "Manager" or role == "manager":

        experience = int(input("Enter Experience (Years): "))

        if experience > 5:
            print("Access Level: DEPARTMENT ACCESS")
        else:
            print("Access Denied")

    elif role == "Employee" or role == "employee":

        experience = int(input("Enter Experience (Years): "))

        if experience > 2:
            print("Access Level: LIMITED ACCESS")
        else:
            print("Access Denied")

    elif role == "Guest" or role == "guest":
        print("Access Level: READ-ONLY ACCESS")

    else:
        print("Invalid Role")
        print("-----------------------------------------")
"""Output:
-------------------------------------------------------
Enter Role: admin
Account Status (Active/Inactive): Active
-------------------------------------------------------
Enter Security Clearance: 4
Access Denied
-------------------------------------------------------
"""