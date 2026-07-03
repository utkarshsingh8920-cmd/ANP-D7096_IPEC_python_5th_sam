"""WAP to create a tuple of 15 numbers given by user and display the odd numbers present in tuple"""

number_list=[]
for x in range (15):

    num=int(input("Enter numbers : "))

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
    if element%2==0:
        print(element,end=',')    