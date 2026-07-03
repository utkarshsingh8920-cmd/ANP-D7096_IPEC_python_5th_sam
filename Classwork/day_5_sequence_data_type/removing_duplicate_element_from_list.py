"""
Removing duplicates element from list
 """
# Create an empty list
numbers = []
# Input elements into the list
for i in range(5):
    #input of element from user 
    num = int(input(f"Enter element  Index number({i+0}) : "))
    #inserting data in list by 
    numbers.append(num)


element = int(input("Enter the element you want to remove duplicates :" ))
print ("The frequency of element you want to remove :-",numbers.count(element))
freq = numbers.count(element)
if (freq==0):
    print(element,"not found")
elif(freq==1):
    print("No dublicates")
else:
    numbers.reverse()
    for x in range(1,element):
        numbers.remove(element)
    numbers.reverse()

print("new list is ",numbers)

"""
Output :
Enter element  Index number(0) : 2
Enter element  Index number(1) : 3
Enter element  Index number(2) : 4
Enter element  Index number(3) : 5
Enter element  Index number(4) : 2
Enter the element you want to remove duplicates :5
The frequency of element you want to remove :- 1
No dublicates
new list is  [2, 3, 4, 5, 2]
"""