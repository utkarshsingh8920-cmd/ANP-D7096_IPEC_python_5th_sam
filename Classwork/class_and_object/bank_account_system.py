"""
Problem 2: Bank Account System 
Problem Statement 
Create a simple Bank Account class that allows users to deposit and withdraw money. 
Requirements 
1. Create a class BankAccount.  
2. Define the following instance variables:  
o account_number  
o customer_name  
o balance  
3. Create the following methods:  
o accept_details() -  Accept account details from the user.  
o deposit(amount) - Add the amount to the balance.  
o withdraw(amount) - Deduct the amount if sufficient balance is available; otherwise 
display "Insufficient Balance".  
o display_balance() - Display account details and current balance.  
4. Create an object of the class.  
5. Accept a deposit amount and a withdrawal amount from the user and perform both operations.  
Sample Input 
Enter Account Number : 1001 
Enter Customer Name : Anjali 
Enter Initial Balance : 5000 
 
Enter Deposit Amount : 2000 
Enter Withdrawal Amount : 4500 
Expected Output 
Deposit Successful. 
 
Withdrawal Successful. 
 ------ Account Details ------ 
Account Number : 1001 
Customer Name  : Anjali 
Current Balance: 2500 
Sample Output (Insufficient Balance) 
Enter Withdrawal Amount : 9000 
 
Insufficient Balance. 
 ------ Account Details ------ 
Account Number : 1001 
Customer Name  : Anjali 
Current Balance: 7000 
"""
# Class to represent a Bank Account
class BankAccount:

    # Constructor to initialize instance variables
    def __init__(self):
        self.account_number = None   # stores account number
        self.customer_name = None    # stores customer name
        self.balance = None          # stores current balance

    # Method to accept account details from the user
    def accept_details(self):
        self.account_number = input("Enter Account Number : ")   # read account number
        self.customer_name = input("Enter Customer Name : ")      # read customer name
        self.balance = float(input("Enter Initial Balance : "))   # read initial balance

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance = self.balance + amount   # add amount to balance
        print("Deposit Successful.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.balance:              # check if sufficient balance
            self.balance = self.balance - amount   # deduct amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")       # not enough balance

    # Method to display account details and balance
    def display_balance(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_number)   # print account number
        print("Customer Name  :", self.customer_name)     # print customer name
        print("Current Balance:", self.balance)           # print current balance


# ---------- Main Program ----------
acc = BankAccount()         # create object of BankAccount class
acc.accept_details()        # accept account details from user

deposit_amount = float(input("Enter Deposit Amount : "))       # read deposit amount
withdrawal_amount = float(input("Enter Withdrawal Amount : ")) # read withdrawal amount

acc.deposit(deposit_amount)        # perform deposit
acc.withdraw(withdrawal_amount)    # perform withdrawal

acc.display_balance()              # display final account details
"""
Output :

Enter Account Number : 1001
Enter Customer Name : rahul
Enter Initial Balance : 5000
Enter Deposit Amount : 2000
Enter Withdrawal Amount : 4500
Deposit Successful.
Withdrawal Successful.

------ Account Details ------
Account Number : 1001
Customer Name  : rahul
Current Balance: 2500.0
"""