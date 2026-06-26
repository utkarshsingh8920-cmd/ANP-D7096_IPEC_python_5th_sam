"""-------------------Problem Statement------------------------------ 
A hospital prioritizes patients based on: 
• Critical Condition  
• Age  
• Oxygen Level  
Rules: 
• Critical condition → Immediate Treatment  
• Oxygen below 90 → High Priority  
• Age above 65 → Medium Priority  
• Others → Normal Priority 
--------------------------------------------------------------------- 
Sample Input 
Critical Condition (Y/N): N 
Age: 70 
Oxygen Level: 94 
--------------------------------------------------------------------
Sample Output 
Patient Priority: Medium Priority 
Reason: Senior Citizen
-------------------------------------------------------------------
 """
#-----------------------Coding-------------------------------------
# Hospital Emergency Triage System
print("---------------------------------------------------")
critical = input("Critical Condition (Y/N): ")
age = int(input("Enter Age: "))
oxygen = int(input("Enter Oxygen Level: "))
print("---------------------------------------------------")

# Validation
if age < 0 or oxygen < 0 or oxygen > 100:
    print("Invalid Input")
    print("---------------------------------------------------")

else:

    if critical == "Y" or critical == "y":
        print("Patient Priority: Immediate Treatment")
        print("---------------------------------------------------")

    elif oxygen < 90:
        print("Patient Priority: High Priority")
        print("Reason: Oxygen below 90")
        print("---------------------------------------------------")

    elif age > 65:
        print("Patient Priority: Medium Priority")
        print("Reason: Senior Citizen")
        print("---------------------------------------------------")

    else:
        print("Patient Priority: Normal Priority")
        print("---------------------------------------------------")
"""Output:
---------------------------------------------------
Critical Condition (Y/N): y
Enter Age: 89
Enter Oxygen Level: 60
---------------------------------------------------
Patient Priority: Immediate Treatment
---------------------------------------------------
"""