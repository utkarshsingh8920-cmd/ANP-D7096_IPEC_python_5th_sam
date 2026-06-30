"""Find sum of 10 numbers"""
#creating a list:-
number=[40,90,34,55,33,54,545,343,43,452]
#Display number to user
print("Number are :")
print(*number)
#finding sum
sum = 0
for x in number:
    sum=sum+x
print("Sum:-",sum)