
"""Develop a menu-driven Python application that demonstrates the use of User-Defined 
Modules and Functions. 
Requirements 
You are required to create a Python module named twodfigures.py that contains functions to perform 
the following calculations for different two-dimensional shapes: 
• Triangle 
o Calculate Area 
o Calculate Perimeter 
• Circle 
o Calculate Area 
o Calculate Circumference (Perimeter) 
• Square 
o Calculate Area 
o Calculate Perimeter 
• Rectangle 
o Calculate Area 
o Calculate Perimeter """
def triangle_area(a,b):
    return (1/2)*a*b

def triangle_perimeter(a,b,c):
    return (a+b+c)

def circle_area (r):
    return (22/7)*r**2
def circle_perimeter(r):
    return (2*(22/7)*r)
    

def square_area(a):
    return a**2
def square_perimeter(a):
    return 4*a

def Rectangle_area(a,b):
    return a*b
def Rectangle_perimeter(a,b):
    return 2*(a*b)
    