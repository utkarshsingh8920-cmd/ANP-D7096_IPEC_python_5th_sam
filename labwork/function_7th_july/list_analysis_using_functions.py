"""
Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list. 
"""
def find_max(numbers):
    """Return the maximum value in the list."""
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_min(numbers):
    """Return the minimum value in the list."""
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def find_average(numbers):
    """Return the average of the list."""
    return sum(numbers) / len(numbers)

#main program 
# main program
# create an empty list first
numbers = []          

for i in range(10):
    num = int(input("Enter any number : "))
    numbers.append(num)   

print("Max number is :", find_max(numbers))
print("Min number is :", find_min(numbers))
print("Average number is : ", find_average(numbers))
"""
Output :
Enter any number : 23
Enter any number : 4234
Enter any number : 23
Enter any number : 4
Enter any number : 3
Enter any number : 43
Enter any number : 43
Enter any number : 34
Enter any number : 34
Enter any number : 34
Max number is : 4234
Min number is : 3
Average number is :  447.5
"""