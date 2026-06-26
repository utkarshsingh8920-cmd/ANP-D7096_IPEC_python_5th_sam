"""
---------------------Problem Statement-----------------------------
A login system validates: 
• Username  
• Password  
• OTP  
Conditions: 
• All correct → Login Successful  
• Incorrect OTP → Re-enter OTP  
• Incorrect Password after 3 attempts → Account Locked  
• Incorrect Username → User Not Found  
---------------------------------------------------------------------
Sample Input 
Username: admin 
Password: admin123 
OTP: 4567 
Sample Output 
Login Successful 
Welcome Admin"""
#-----------------------Coding-------------------------------------
# Cybersecurity Login Validation
#-------------------- Correct Login Details---------------------------
correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"

# Input Username
print("-----------------------------------------------")
username = input("Enter Username: ")

# Check Username
if username != correct_username:
    print("-----------------------------------------------")
    print("User Not Found")
    print("-----------------------------------------------")

else:
    attempts = 0

    # Allow only 3 password attempts
    while attempts < 3:
        password = input("Enter Password: ")

        if password == correct_password:
            otp = input("Enter OTP: ")

            if otp == correct_otp:
                print("-----------------------------------------------")
                print("Login Successful")
                print("Welcome Admin")
                print("-----------------------------------------------")
            else:
                print("Re-enter OTP")
            break

        else:
            attempts += 1
            print("Incorrect Password")

    if attempts == 3:
        print("-----------------------------------------------")
        print("Account Locked")
        print("-----------------------------------------------")
        
"""
Output :
-----------------------------------------------
Enter Username: admin
Enter Password: admin123
Enter OTP: 4567
-----------------------------------------------
Login Successful
Welcome Admin
-----------------------------------------------
"""
