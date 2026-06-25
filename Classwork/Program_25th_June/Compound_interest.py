"Calculat the compound interest"
#------------------------------------------------------------
principal = float(input("Enter Principal Amount: "))
if principal < 0 :
    exit("Error: Values cannot be negative.")
rate = float(input("Enter Annual Interest Rate (%): "))
if  rate < 0 :
    exit("Error: Values cannot be negative.")
time = float(input("Enter Time (in years): "))
if  time < 0:
    exit("Error: Values cannot be negative.")
#---------------------------------------------------------------
else:
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal

    print("Compound Interest =", round(( principal * (1 + rate / 100) ** time) - principal, 2))
    print("Total Amount =", round( principal * (1 + rate / 100) ** time, 2))