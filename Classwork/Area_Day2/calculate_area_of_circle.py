''' Write a program to calculate area of circle and validate it'''
radius = float(input("Enter the radius of the circle: "))
#----------------------------------------
print  ("----------------------------------------")
print ("The radius of circle is = ",radius)
if radius <= 0:
    print("Error: Radius cannot be negative or .")
else:
     print("Area of the circle =",3.15*radius**2)
'''Output:
Enter the length of the rectangle: 12
------------------------------------------
The radius of circle is =  12.0
Area of the circle = 453.59999999999997'''