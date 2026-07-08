#Define a class to perform operations on rectangle 
class rectangle:
    #member variable
    length = 0
    breath = 0
    #Method to initalize data 
    def initalize(self,l,b):
        self.length=l
        self.breath=b
    #method to display data 
    def display_data(self):
        print("--------Rectangle-----------")
        print ("length : ",self.length,"cm")
        print("Breath : ",self.breath   ,"cm")
#Object creation 
rect = rectangle()
rect.initalize(20,50)
rect.display_data()

"""Output:
--------Rectangle-----------
length :  20 cm
Breath :  50 cm
"""
