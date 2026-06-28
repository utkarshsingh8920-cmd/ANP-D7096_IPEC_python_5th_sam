"""---------------------Problem Statement------------------------------ 
An electricity department categorizes households based on monthly electricity consumption. 
• Up to 100 units → Low Consumption  
• 101-300 units → Moderate Consumption  
• Above 300 units → High Consumption  
Write a Python program to display the consumption category. 
-----------------------------------------------------------------------
Sample Input 
245 
-----------------------------------------------------------------------
Sample Output 
Moderate Consumption
 """
#----------------------------Coding section-----------------------------
# Electricity Consumption Category 
# Electricity Consumption Category
print("-------------------------------------------------------------")
units = int(input("Enter the monthly electricity consumption (units): "))
#---------------------------Chaking for validation-------------------
if units<0:
    print("Enter correct electricity consumption (units)")
#---------------------------Chaking Condition-----------------------
elif units <= 100:
    print("Low Consumption")
elif units <= 300:
    print("Moderate Consumption")
else:
    print("High Consumption")
print("-------------------------------------------------------------")
#--------------------------------------------------------------------------
"""Output :
-------------------------------------------------------------
Enter the monthly electricity consumption (units): 57
Low Consumption
-------------------------------------------------------------
"""