"""-----------------Problem Statement------------------------------
Only vehicles having a valid parking pass are allowed to enter a private parking area. 
Accept either 1 (Valid Pass) or 0 (No Pass). 
• If the input is 1, display: 
Entry Allowed 
• Otherwise display: 
Entry Denied 
------------------------------------------------------------------
Sample Input 
0 
-------------------------------------------------------------------
Sample Output 
Entry Denied 
"""
#------------------------------Coding-----------------------------------
# Parking Entry Validation
print("---------------------------------------------------------------")
parking_pass = int(input("Enter 1 for Valid Pass or 0 for No Pass: "))
#------------------------Condition check---------------------------------
if parking_pass == 1:
    print("Entry Allowed")
else:
    print("Entry Denied")

print("---------------------------------------------------------------")
"""Output :
---------------------------------------------------------------
Enter 1 for Valid Pass or 0 for No Pass: 1
Entry Allowed
---------------------------------------------------------------
"""
