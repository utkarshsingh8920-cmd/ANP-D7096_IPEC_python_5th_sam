"""
-----------------------------Problem Statement-----------------------------------------------------
A customer keeps entering transaction amounts. 
Positive numbers indicate deposits, while negative numbers indicate withdrawals. 
The customer enters 0 to finish.
------------------------------------------------------------ 
Display: 
• Total Deposit  
• Total Withdrawal  
• Final Balance
"""
#--------------------- Banking Transaction Program ---------------------

# Initialize variables to store total deposits, withdrawals, and balance
deposit = 0
withdrawal = 0
balance = 0

# Ask the user to enter the first transaction amount
# Enter 0 to stop entering transactions
amount = float(input("Enter Transaction (0 to Stop): "))

# Repeat until the user enters 0
while amount != 0:

    # If the transaction amount is positive, it is a deposit
    if amount > 0:
        deposit += amount

    # If the transaction amount is negative, it is a withdrawal
    else:
        withdrawal += abs(amount)   # abs() converts the negative value to positive

    # Update the account balance
    balance += amount

    # Ask the user to enter the next transaction
    amount = float(input("Enter Transaction (0 to Stop): "))

# Display the final results
print("Total Deposit =", deposit)
print("Total Withdrawal =", withdrawal)
print("Final Balance =", balance)

#-------------------------------------------------------------------
"""
Output :
Enter Transaction (0 to Stop): 100
Enter Transaction (0 to Stop): -12
Enter Transaction (0 to Stop): 1333
Enter Transaction (0 to Stop): -4342
Enter Transaction (0 to Stop): 0
Total Deposit = 1433.0
Total Withdrawal = 4354.0
Final Balance = -2921.0
"""
