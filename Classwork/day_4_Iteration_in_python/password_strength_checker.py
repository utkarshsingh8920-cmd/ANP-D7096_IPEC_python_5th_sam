"""---------------------------Problem Statement-----------------------------------------------
A website requires users to create a password having at least 8 characters. 
Keep asking the user to enter a password until the entered password satisfies the minimum length 
requirement.
------------------------------------------------------------------------- 
Sample Output 
Enter Password: hello 
Password too short. 
 
Enter Password: python@123 
Password Accepted.
--------------------------------------------------------------------------
"""
#-------------------------------------------------------------------------
password = ""
#-------------------------------------------------------------------------
while len(password) < 8:
    password = input("Enter Password: ")
    if len(password) < 8:
        # password less then 8
        print("Password too short.")
    #password accepted   
    else:
        print("Password Accepted.")
#-----------------------------------------------------------------------
"""Output :
Enter Password: 232232
Password too short.
Enter Password: 328949843
Password Accepted.
"""
