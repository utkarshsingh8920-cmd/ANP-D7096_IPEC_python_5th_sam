""" Program to count eligible voters using for loop with validation """

ages = []

# Taking input for 10 people
for i in range(10):
    age = int(input(f"Enter age of person {i+1}: "))

    # Validation using for loop logic
    if age < 0:
        print("Invalid age! Setting it to 0.")
        age = 0

    ages.append(age)

# Counting eligible voters using for loop
count = 0
for age in ages:
    if age >= 18:
        count += 1

# Displaying results
print("\n------ Result ------")
print("List of Ages:", ages)
print("Total Eligible for Voting:", count)
#---------------------------------------------------------
"""
Output :
Enter age of person 1: 23
Enter age of person 2: 32
Enter age of person 3: 43
Enter age of person 4: 54
Enter age of person 5: 7
Enter age of person 6: 34
Enter age of person 7: 19
Enter age of person 8: 14
Enter age of person 9: 12
Enter age of person 10: 15

------ Result ------
List of Ages: [23, 32, 43, 54, 7, 34, 19, 14, 12, 15]
Total Eligible for Voting: 6
"""