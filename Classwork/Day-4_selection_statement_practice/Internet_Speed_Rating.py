"""Problem Statement 
An Internet Service Provider categorizes connection quality based on download speed. 
• Less than 25 Mbps → Slow  
• 25 - 99 Mbps → Good  
• 100 Mbps or above → Excellent  
Write a Python program to display the connection quality. 
Sample Input 
120 
Sample Output 
Excellent Connection"""
#----------------------------Coding section-------------------------
# Internet Speed Rating
print("-------------------------------------------------------------")
speed = float(input("Enter download speed (Mbps): "))
#-------------------------Chaking for validation---------------------
if speed<0:
    exit("Enter positive value only")
#--------------------------Chaking condition-----------------------
if speed < 25:
    print("Slow Connection")
elif speed < 100:
    print("Good Connection")
else:
    print("Excellent Connection")
print("-------------------------------------------------------------")
#---------------------------------------------------------------------
"""Output :
-------------------------------------------------------------
Enter download speed (Mbps): 60
Good Connection
-------------------------------------------------------------
"""