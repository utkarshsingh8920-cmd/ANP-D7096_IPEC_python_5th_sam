"""
 -----------------------------------Problem Statement:------------------------------------
Create a dictionary where: 
• Employee ID is the key.  
• Value is another dictionary containing:  
o Name  
o Department  
o Salary  
Perform the following operations: 
• Display all employee details.  
• Search for an employee using Employee ID.  
• Increase the salary of all employees by 10%.  
• Display employees belonging to a specific department entered by the user."""

# Dictionary of employees
# Dictionary of employees (nested dictionary)
employees = {
    101: {"Name": "Alice", "Department": "IT", "Salary": 50000},
    102: {"Name": "Bob", "Department": "HR", "Salary": 40000},
    103: {"Name": "Charlie", "Department": "IT", "Salary": 55000},
    104: {"Name": "David", "Department": "Finance", "Salary": 60000},
    105: {"Name": "Emma", "Department": "HR", "Salary": 45000}
}

while True:
    print("\n===== MENU =====")
    print("1. Display all employee details")
    print("2. Search employee by ID")
    print("3. Increase salary of all employees by 10%")
    print("4. Display employees by department")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- All Employee Details ---")
        for emp_id in employees:
            details = employees[emp_id]
            print(f"ID: {emp_id}, Name: {details['Name']}, "
                  f"Department: {details['Department']}, Salary: {details['Salary']}")

    elif choice == "2":
        search_id = int(input("Enter Employee ID to search: "))
        if search_id in employees:
            details = employees[search_id]
            print(f"\nID: {search_id}, Name: {details['Name']}, "
                  f"Department: {details['Department']}, Salary: {details['Salary']}")
        else:
            print("Employee ID not found.")

    elif choice == "3":
        for emp_id in employees:
            employees[emp_id]["Salary"] = employees[emp_id]["Salary"] * 1.10
        print("\nSalaries increased by 10% for all employees.")
        for emp_id in employees:
            details = employees[emp_id]
            print(f"ID: {emp_id}, Name: {details['Name']}, "
                  f"Department: {details['Department']}, Salary: {details['Salary']:.2f}")

    elif choice == "4":
        dept = input("Enter department name: ")
        print(f"\n--- Employees in {dept} Department ---")
        found = False
        for emp_id in employees:
            if employees[emp_id]["Department"].lower() == dept.lower():
                details = employees[emp_id]
                print(f"ID: {emp_id}, Name: {details['Name']}, Salary: {details['Salary']}")
                found = True
        if not found:
            print("No employees found in this department.")

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

"""
Output :
===== MENU =====
1. Display all employee details
2. Search employee by ID
3. Increase salary of all employees by 10%
4. Display employees by department
5. Exit
Enter your choice (1-5): 1

--- All Employee Details ---
ID: 101, Name: Alice, Department: IT, Salary: 50000
ID: 102, Name: Bob, Department: HR, Salary: 40000
ID: 103, Name: Charlie, Department: IT, Salary: 55000
ID: 104, Name: David, Department: Finance, Salary: 60000
ID: 105, Name: Emma, Department: HR, Salary: 45000

===== MENU =====
1. Display all employee details
2. Search employee by ID
3. Increase salary of all employees by 10%
4. Display employees by department
5. Exit
Enter your choice (1-5): 2
Enter Employee ID to search: 102

ID: 102, Name: Bob, Department: HR, Salary: 40000

===== MENU =====
1. Display all employee details
2. Search employee by ID
3. Increase salary of all employees by 10%
4. Display employees by department
5. Exit
Enter your choice (1-5): 
"""