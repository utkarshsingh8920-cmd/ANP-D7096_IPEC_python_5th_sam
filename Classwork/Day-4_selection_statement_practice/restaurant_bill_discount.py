"""--------------Problem Statement-----------------------------------
A restaurant offers discounts based on the total bill amount. 
• Bill below ₹1000 → No Discount  
• ₹1000 - ₹2999 → 10% Discount  
• ₹3000 or more → 20% Discount  
Write a Python program to determine the applicable discount. 
Sample Input 
3200 
Sample Output 
20% Discount Applied"""
#-------------------Coding------------------------------------------
# Restaurant Bill Discount
print("------------------------------------------------------------")
bill = float(input("Enter the total bill amount: ₹"))
#---------------------Validating user input-------------------------
if bill<0:
    exit("Amount can not be negative ")
#--------------------------For chacking conditon------------------------
if bill < 1000:
    print("No Discount")
elif bill < 3000:
    print("10% Discount Applied")
else:
    print("20% Discount Applied")

print("---------------------------------------------------------")

"""
Output :
------------------------------------------------------------
Enter the total bill amount: ₹45400
20% Discount Applied
---------------------------------------------------------
"""