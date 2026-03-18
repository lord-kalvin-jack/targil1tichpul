#
#  Example program for Targil 1
#binyamin godfrey 218804581
import math
from myboolfuncs import *
#
# Area calculation program  
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
#
def squarePyramidVolume(radius):
    return 4/3*math.pi*radius**3
#
def squarePyramidVolume(base, height):
    return base*height*base/3
#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# calculates if the triangle lengths are correct
def isTriangle(a,b,c):
    if a==0 or b==0 or c==0:
        return False
    else:
        if a+b<c or b+c<a or c+a<b:
            return False
        else:
            return True

#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")  
# Print out the menu
shapes = ("Rectangle", "Circle","Square","Triangle","Sphere","Square-Pyramid")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes) 
    # Get the user's choice: 
    shape = input("> ")
    # Calculate the area: 
    if shape == "1":
         height = getNumber("Please enter the height: ")    
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":
        width = getNumber("Please enter the width: ")
        area=rectangleArea(width, width)
        print("The area is", area)
        continue
    elif shape == "4":
        base=getNumber("Please enter the base: ")
        square_hight = getNumber("Please enter the height: ")
        area = rectangleArea(base,hight )/2
        print("The area is", area)
        continue
    elif shape == "5":
        radius = getNumber("Please enter the radius: ")

    elif shape == "6":
        base=getNumber("Please enter the base: ")
        hight = getNumber("Please enter the height: ")
        area = squarePyramidVolume(base,hight)
        print("The area is", area)
        continue
    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")
