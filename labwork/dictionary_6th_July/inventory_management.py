"""
Problem Statement: 
Create a dictionary to maintain the stock of products in a shop. 
Example: 
{ 
'Laptop': 15, 
'Mouse': 40, 
'Keyboard': 25, 
'Monitor': 10 
} 
Implement the following: 
• Add a new product.  
• Update the stock of an existing product.  
• Remove a product from inventory.  
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
• Display products having stock less than 20.  
• Display the total number of items available in the inventory
"""
# Dictionary to store stock of products
inventory = {
    'Laptop': 15,
    'Mouse': 40,
    'Keyboard': 25,
    'Monitor': 10
}

while True:
    print("\n===== MENU =====")
    print("1. Display all products")
    print("2. Add a new product")
    print("3. Update stock of a product")
    print("4. Remove a product")
    print("5. Display products with stock less than 20")
    print("6. Display total items in inventory")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("\n--- Current Inventory ---")
        for product in inventory:
            print(f"{product}: {inventory[product]}")

    elif choice == "2":
        new_product = input("Enter new product name: ")
        if new_product in inventory:
            print(f"{new_product} already exists. Use update instead.")
        else:
            new_stock = int(input("Enter stock quantity: "))
            inventory[new_product] = new_stock
            print(f"{new_product} added with stock {new_stock}.")

    elif choice == "3":
        update_product = input("Enter product name to update: ")
        if update_product in inventory:
            new_stock = int(input("Enter new stock quantity: "))
            inventory[update_product] = new_stock
            print(f"{update_product}'s stock updated to {new_stock}.")
        else:
            print(f"{update_product} not found.")

    elif choice == "4":
        remove_product = input("Enter product name to remove: ")
        if remove_product in inventory:
            del inventory[remove_product]
            print(f"{remove_product} removed from inventory.")
        else:
            print(f"{remove_product} not found.")

    elif choice == "5":
        print("\n--- Products with stock less than 20 ---")
        found = False
        for product in inventory:
            if inventory[product] < 20:
                print(f"{product}: {inventory[product]}")
                found = True
        if not found:
            print("No products with stock less than 20.")

    elif choice == "6":
        total_items = sum(inventory.values())
        print(f"\nTotal items in inventory: {total_items}")

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

"""
Output :
===== MENU =====
1. Display all products
2. Add a new product
3. Update stock of a product
4. Remove a product
5. Display products with stock less than 20
6. Display total items in inventory
7. Exit
Enter your choice (1-7): 1

--- Current Inventory ---
Laptop: 15
Mouse: 40
Keyboard: 25
Monitor: 10

===== MENU =====
1. Display all products
2. Add a new product
3. Update stock of a product
4. Remove a product
5. Display products with stock less than 20
6. Display total items in inventory
7. Exit
Enter your choice (1-7): 2
Enter new product name: mobile
Enter stock quantity: 3
mobile added with stock 3.

===== MENU =====
1. Display all products
2. Add a new product
3. Update stock of a product
4. Remove a product
5. Display products with stock less than 20
6. Display total items in inventory
7. Exit
Enter your choice (1-7): 
"""