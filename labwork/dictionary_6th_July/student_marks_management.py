"""
-------------------------------------------Problem Statement---------------------------------------------------
Create a dictionary to store the marks of 5 students, where the key is the student's name and the 
value is their marks. 
Perform the following operations: 
• Display all student names and marks.  
• Add a new student with marks.  
• Update the marks of an existing student.  
• Delete a student by name.  
• Display the student who scored the highest marks.
  """

#----------------------------------------------------------------------------------------------

# Dictionary to store marks of 5 students
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Emma": 78
}

while True:
    print("\n===== MENU =====")
    print("1. Display all students")
    print("2. Add a new student")
    print("3. Update a student's marks")
    print("4. Delete a student")
    print("5. Display highest scorer")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\n--- Student Marks ---")
        for name in students:
            print(f"{name}: {students[name]}")

    elif choice == "2":
        new_name = input("Enter new student's name: ")
        if new_name in students:
            print(f"{new_name} already exists.")
        else:
            new_marks = int(input("Enter marks: "))
            students[new_name] = new_marks
            print(f"{new_name} added with marks {new_marks}.")

    elif choice == "3":
        update_name = input("Enter student name to update: ")
        if update_name in students:
            updated_marks = int(input("Enter new marks: "))
            students[update_name] = updated_marks
            print(f"{update_name}'s marks updated to {updated_marks}.")
        else:
            print(f"{update_name} not found.")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")
        if delete_name in students:
            del students[delete_name]
            print(f"{delete_name} deleted from records.")
        else:
            print(f"{delete_name} not found.")

    elif choice == "5":
        top_student = None
        top_marks = -1
        for name in students:
            if students[name] > top_marks:
                top_marks = students[name]
                top_student = name
        print(f"Highest scorer: {top_student} with {top_marks} marks.")

    elif choice == "6":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

"""
Output:
===== MENU =====
1. Display all students
2. Add a new student
3. Update a student's marks
4. Delete a student
5. Display highest scorer
6. Exit
Enter your choice (1-6): 1

--- Student Marks ---
Alice: 85
Bob: 72
Charlie: 90
David: 65
Emma: 78

===== MENU =====
1. Display all students
2. Add a new student
3. Update a student's marks
4. Delete a student
5. Display highest scorer
6. Exit
Enter your choice (1-6): 4
Enter student name to delete: Emma
Emma deleted from records.

===== MENU =====
1. Display all students
2. Add a new student
3. Update a student's marks
4. Delete a student
5. Display highest scorer
6. Exit
Enter your choice (1-6): 
"""