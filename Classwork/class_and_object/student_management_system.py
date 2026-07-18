"""
Problem 1: Student Management System 
Problem Statement 
Create a class named Student to store and display a student's details. 
Requirements 
1. Create a class Student.  
2. Define the following instance variables:  
o student_id  
o name  
o course  
o marks  
3. Create a method accept_data() to take input from the user.  
4. Create a method display_data() to display all student details.  
5. Create another method check_result() that:  
o Displays "Pass" if marks are 35 or above  
o Displays "Fail" otherwise.  
6. Create an object of the class and call all the methods.  
Sample Input 
Enter Student ID : 101 
Enter Name : Rahul 
Enter Course : Python 
Enter Marks : 78 
Expected Output ------ Student Details ------ 
Student ID : 101 
Name       : Rahul 
Course     : Python 
Marks      : 78 
Result     : Pass
"""
#Creating Class for Student:
# Class to store and display student details
class Student:

    # Constructor to initialize instance variables
    def __init__(self):
        self.student_id = None   # stores student ID
        self.name = None         # stores student name
        self.course = None       # stores course name
        self.marks = None        # stores marks obtained

    # Method to take input from the user
    def accept_data(self):
        self.student_id = input("Enter Student ID : ")   # read student ID
        self.name = input("Enter Name : ")                # read student name
        self.course = input("Enter Course : ")             # read course name
        self.marks = int(input("Enter Marks : "))          # read marks as integer

    # Method to display all student details
    def display_data(self):
        print("\n------ Student Details ------")
        print("Student ID :", self.student_id)   # print student ID
        print("Name       :", self.name)          # print student name
        print("Course     :", self.course)        # print course name
        print("Marks      :", self.marks)         # print marks

    # Method to check and display result based on marks
    def check_result(self):
        if self.marks >= 35:          # condition for passing
            print("Result     : Pass")
        else:                          # condition for failing
            print("Result     : Fail")


# ---------- Main Program ----------
s1 = Student()          # create object of Student class
s1.accept_data()        # call method to accept data
s1.display_data()       # call method to display data
s1.check_result()       # call method to check and display result
"""
Output :
------ Student Details ------
Student ID : 123
Name       : Rahul
Course     : B.tech
Marks      : 89
Result     : Pass
"""