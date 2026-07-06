"""
WAP TO  Count the uppercase and lowercase in string
"""
#input of sentence
sentence = input("Enter any sentence : ")
#initilize uppercase and lowercase count as 0
upper_case=0
lower_case=0
for x in sentence:
    if (x>='A' and x<='Z'):
        upper_case=upper_case+1

    elif(x>='a' and x<='z'):
        lower_case=lower_case+1
        

print( "No of uppercase",upper_case)
print("No of lower case",lower_case)
"""
Output :
Enter any sentence : ABCDabcd
No of uppercase 4
No of lower case 4
"""
