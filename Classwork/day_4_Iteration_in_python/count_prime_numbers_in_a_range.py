"""
Accept two integers representing the starting and ending values of a range. 
Display all prime numbers within the range and finally display the total number of prime numbers 
found. 
"""
#--------------------------------Coding Section-------------------------------------

start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))
#------------------------------------------------------------------------
count = 0

for num in range(start, end + 1):
#
    if num < 2:
        continue

    prime = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = 0
            break

    if prime == 1:
        print(num)
        count += 1

print("Total Prime Numbers =", count)
#--------------------------------------------------------------------
"""
Output :
Enter Ending Number: 15
2
3
5
7
11
13
Total Prime Numbers = 6
"""