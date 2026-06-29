"""
--------------------------------Problem Statement--------------------------------------------------------
A supermarket allows a customer to purchase multiple products. 
The customer first enters the number of products. 
---------------------------------------------------------------
For each product, enter: 
• Product Name  
• Quantity  
• Price per Unit 
------------------------------------------------------------------- 
Finally display: 
• Individual Product Cost  
• Total Bill Amount  
• Most Expensive Product  
• Cheapest Product  
• Average Product Cost
"""
#---------------------------------------------------------------------------
#--------------------------------coding section----------------------------------
#user can enter the number of products
n = int(input("Enter Number of Products: "))

total_bill = 0
#use for loop
for i in range(1, n + 1):

    name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Unit: "))

    cost = quantity * price

    print("Product Cost =", cost)

    total_bill += cost

    if i == 1:
        highest_cost = lowest_cost = cost
        expensive = cheap = name
    else:
        if cost > highest_cost:
            highest_cost = cost
            expensive = name

        if cost < lowest_cost:
            lowest_cost = cost
            cheap = name

print("\nTotal Bill =", total_bill)
print("Most Expensive Product =", expensive)
print("Cheapest Product =", cheap)
print("Average Product Cost =", total_bill / n)
#--------------------------------------------------------------------------------------------
"""
Output :
Enter Number of Products: 2
Product Name: cola
Quantity: 2
Price per Unit: 100
Product Cost = 200.0
Product Name: chips
Quantity: 2
Price per Unit: 10
Product Cost = 20.0

Total Bill = 220.0
Most Expensive Product = cola
Cheapest Product = chips
Average Product Cost = 110.0
"""
