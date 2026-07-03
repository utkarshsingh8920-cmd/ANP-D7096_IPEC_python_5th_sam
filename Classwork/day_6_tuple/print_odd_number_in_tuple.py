"""WAP to create a tuple of 15 numbers given by user and display the odd numbers present in tuple"""

number_list=[]
for x in range (15):
    # input of number 
    num=int(input("Enter numbers : "))
    # inserting into list
    number_list.append(num)

#---------------------------------------------------
#Creating a tuple from list 
number = tuple(number_list)
print("--------------------------------------")
print("Tuple of a number are")
print(number)
#Display odd number
print("---------------------------------------")
print("Odd number in tuple ")
for element in number:
    #for printing odd number 
    if element%2==0:
        print(element,end=',')    

"""
Output :
Enter numbers : 3
Enter numbers : 1
Enter numbers : 2
Enter numbers : 3
Enter numbers : 4
Enter numbers : 5
Enter numbers : 6
Enter numbers : 7
Enter numbers : 8
Enter numbers : 9
Enter numbers : 0
Enter numbers : 1
Enter numbers : 2
Enter numbers : 3
Enter numbers : 4
--------------------------------------
Tuple of a number are
(3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4)
---------------------------------------
Odd number in tuple 
2,4,6,8,0,2,4,
"""