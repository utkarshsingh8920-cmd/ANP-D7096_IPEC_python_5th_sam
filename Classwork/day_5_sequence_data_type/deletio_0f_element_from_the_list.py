"""deletio_0f_element_from_the_list
write a program to enter number by user in list then user can remove any element from list by using pop()"""
# ------------------ Remove Element from List using pop() ------------------

# Create an empty list
numbers = []
size = int(input("Enter size of list: "))
# Input elements into the list
for i in range(size):
    #input of element from user 
    num = int(input(f"Enter element  Index number({i+0}) : "))
    #inserting data in list by 
    numbers.append(num)

print ("List is :",numbers)
# for removing element from list 
print("-------------------------------------------")
x=int(input("Enter index number of the element to remove : "))
numbers.pop(x)
print("New list is ",numbers)
""" 
Output :
Enter size of list: 5
Enter element  Index number(0) : 23
Enter element  Index number(1) : 34
Enter element  Index number(2) : 45
Enter element  Index number(3) : 34
Enter element  Index number(4) : 54
List is : [23, 34, 45, 34, 54]
-------------------------------------------
Enter index number of the element to remove : 4
New list is  [23, 34, 45, 34]
"""
