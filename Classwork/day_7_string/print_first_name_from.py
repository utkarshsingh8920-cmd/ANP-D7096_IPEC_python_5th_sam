"""WAP To ask the user to input the name and display the 1st name from it without using the library method"""
#name enter by user
full_name = input("Enter your full name: ")

first_name = " "
for ch in full_name:
    #as soon as we hit space the loop is break
    if ch == " ":
        break
    first_name += ch

print("Your first name is:", first_name)
"""
Output :
"""