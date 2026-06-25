"""Write a program to calculate Speed"""
distance = float(input("Enter distance travelled (in meters): "))
if distance < 0:
    exit("Error: Distance cannot be negative.")
time = float(input("Enter time taken (in seconds): "))
if time <= 0:
    exit("Error: Time must be greater than 0.")
else:
    print("-------------------------------------")
    print ("Given Distance is = ",distance)
    print ("Given time is",time)
    print ("-------------------------------------")
    print("Speed =",distance/time,"m/s")
    """Output :
    Enter distance travelled (in meters): 34
    Enter time taken (in seconds): 34
    -------------------------------------
    Given Distance is =  34.0
    Given time is 34.0
    -------------------------------------
    Speed = 1.0 m/s
    """
   