"""--------------------Problem Statement----------------------------------
A smartphone displays a low battery warning only when the battery percentage falls below 15%. 
Write a Python program to accept the battery percentage. 
If the battery is below 15, display: 
Connect Charger Immediately 
Otherwise, display nothing.
------------------------------------------------------------- 
Sample Input 
10 
--------------------------------------------------------------
Sample Output 
Connect Charger Immediately 
"""
# Smartphone Low Battery Warning
print("------------------------------------------------")
battery = int(input("Enter the battery percentage: "))
#----------------------Chacking validation-----------------------------
if battery<0:
    exit("Mobile battery can not negative")
#------------------- Chacking condition given by user----------------------
if battery < 15:
    print("Connect Charger Immediately")
else:
    print("If you want you can connect charger ")
#----------------------------------------------------------------------
print("------------------------------------------------")
"""Output:
------------------------------------------------
Enter the battery percentage: 70
If you want you can connect charger 
------------------------------------------------
"""