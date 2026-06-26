"""Problem Statement 
An airline calculates ticket fare using: 
Base Fare = ₹5000 
Additional Charges: 
• Business Class → +₹3000  
• Window Seat → +₹500  
• Weekend Travel → +₹1000  
Discounts: 
• Age below 12 → 50%  
• Age above 60 → 20%  
Calculate the final ticket fare. 
Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y 
Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0
"""
#--------------------Coding-----------------------------------
# Airline Ticket Fare Calculator

# Base fare is fixed
fare = 5000

# Taking input from the user
age = int(input("Enter Passenger Age: "))
print("------------------------------------------")
business = input("Business Class (Y/N): ")
window = input("Window Seat (Y/N): ")
weekend = input("Weekend Travel (Y/N): ")
print("-------------------------------------------")
if age< 0 :
    exit("Age can not be negative")

# Check if Business Class is selected
if business == "Y" or business == "y":
    fare = fare + 3000

# Check if Window Seat is selected
if window == "Y" or window == "y":
    fare = fare + 500

# Check if Weekend Travel is selected
if weekend == "Y" or weekend == "y":
    fare = fare + 1000

# Display Base Fare and Additional Charges
print("Base Fare: ₹5000")
print("Additional Charges: ₹", fare - 5000)

# Apply discount based on age
if age < 12:
    print("Child Discount: 50%")
    fare = fare - (fare * 50 / 100)

elif age > 60:
    print("Senior Citizen Discount: 20%")
    fare = fare - (fare * 20 / 100)

# Display the final fare
print("Final Ticket Fare: ₹", fare)
"""
Output :
Enter Passenger Age: 23
------------------------------------------
Business Class (Y/N): y 
Window Seat (Y/N): y
Weekend Travel (Y/N): y
-------------------------------------------
Base Fare: ₹5000
Additional Charges: ₹ 4500
Final Ticket Fare: ₹ 9500

"""