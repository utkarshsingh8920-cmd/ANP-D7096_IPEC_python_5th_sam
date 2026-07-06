""""""
#input of sentence
sentence = input("Enter any sentence : ")
#initilize vowel count as 0
vowels = 0
for x in sentence:
    if (x=='A' or x=='a' or x=='E' or x=='e'or x=='I' or x=='i' or x=='O' or x=='o' or x=='U' or x=='u'):
        #increment vowel count 
        vowels = vowels+1
#-------------------------------------------------------------------------------------
print("No of vowels = ",vowels)
"""
Output :
Enter any sentence : utkarsh
No of vowels =  2
"""

