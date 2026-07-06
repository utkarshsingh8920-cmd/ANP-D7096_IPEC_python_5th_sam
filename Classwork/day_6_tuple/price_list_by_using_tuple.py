"""
write a program to create a tuple of price of 10 product given by user . Display the lowest price, 
higest price , count the no of product where price is greater than 4000 : along with the price you
are require to store the name of product also while displaying lowest price and higest price display
the name of product along with it
"""
price_list=[]
price_name=[]
price_list=[]
for x in range (10):

    product = input("Enter product name : ")

    price = int(input("Enter price of product : "))

    price_list.append((product,price))

print(price_list)
