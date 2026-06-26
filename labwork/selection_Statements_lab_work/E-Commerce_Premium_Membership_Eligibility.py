"""
-----------------------Problem Statement------------------------------ 
A customer becomes Premium Member if: 
• Total Purchases > ₹50,000  
• Orders Completed ≥ 20  
• Customer Rating ≥ 4.5  
Special Case: 
• Purchases above ₹1,00,000 automatically qualify.  
----------------------------------------------------------------------
Sample Input 
Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 
Sample Output 
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000. 
"""
#---------------------------Codeing-----------------------------------
# Premium Membership Eligibility

print("-------------------------------------------------------")
purchase = float(input("Enter Total Purchases: "))
orders = int(input("Enter Orders Completed: "))
rating = float(input("Enter Customer Rating: "))
print("-------------------------------------------------------")
# Validation
if purchase < 0 or orders < 0 or rating < 0 or rating > 5:
    print("-------------------------------------------------------")
    print("Invalid Input!")
    print("-------------------------------------------------------")

else:

    if purchase > 100000:
        print("-------------------------------------------------------")
        print("Premium Membership Status: Eligible")
        print("Reason: Purchase amount exceeded ₹100000.")
        print("-------------------------------------------------------")

    elif purchase > 50000 and orders >= 20 and rating >= 4.5:
        print("-------------------------------------------------------")
        print("Premium Membership Status: Eligible")
        print("-------------------------------------------------------")

    else:
        print("-------------------------------------------------------")
        print("Premium Membership Status: Not Eligible")
        print("-------------------------------------------------------")
"""Output
"""