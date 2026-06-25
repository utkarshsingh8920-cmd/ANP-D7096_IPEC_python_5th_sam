"""-------Area of triangle----------"""
base = float(input("Enter the base of the triangle: "))
if base <= 0:
    exit("Error: Base must be positive values.")
height = float(input("Enter the height of the triangle: "))

if  height <= 0:
    exit("Error: Base and height must be positive values.")
else:
    print ("--------------------------------------------------")
    print ("The base of triangle is = ",base)
    print ("The hight of trangle is = ",height)
    print("Area of Triangle =", 0.5 * base * height)
 """Output :
    Enter the base of the triangle: 23
    Enter the height of the triangle: 23
    --------------------------------------------------
    The base of triangle is =  23.0
    The hight of trangle is =  23.0
    Area of Triangle = 264.5 
    """
