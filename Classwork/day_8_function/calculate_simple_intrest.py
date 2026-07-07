"""Function to calculate simple interest"""
def calculate_simple_interest(principal,rate,time):
    return (principal*rate*time)/100
#-----------------------------------------------------
#main program
principal = float(input("Enter principal (in Rs): "))
rate = float(input("Enter rate (in %): "))
time = int(input("Enter time : "))
print ("Simple interest : Rs ",calculate_simple_interest(principal,rate,time))
