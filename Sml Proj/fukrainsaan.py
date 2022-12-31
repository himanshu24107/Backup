import math
from project import x
from math import asin, degrees

pi = 22/7

def degtorad():
            var = float(input("Enter your variable:"))
            degtorad = pi/180*var
            print("Your Converted Value is", degtorad)

def radtodeg():
    var2 = float(input("Enter your variable:"))
    radtodeg = (180/pi)*var2
    print("Your Converted Value is", radtodeg)



def pow():
    a = int(input("Enter base no:"))
    b = int(input("Enter Power:"))

    pow = math.pow(a,b)

def quad():
    angle = int(input("Enter Angles in degree:"))
    if angle>0:
        if angle == 90:
            print("On Y(+ve) axis")
        elif angle ==180:
            print("On X(-ve) axis")
        elif angle ==270:
            print("On Y(-ve) axis")
        elif angle == 360 or 0:
            print("On X(+ve) axis")
        else:
            alpha = (angle//90)+1
            print("Quadrant:", alpha)
    elif angle<0:
        if angle == 90:
            print("On Y(+ve) axis")
        elif angle ==180:
            print("On X(-ve) axis")
        elif angle ==270:
            print("On Y(-ve) axis")
        elif angle == 360 or 0:
            print("On X(+ve) axis")
        else:    
            alpha = (angle//90)+5
            print("Quadrant:", alpha)


def ratiotodeg():
    rad_angle = int(input("Enter to convert to trigo ratio(deg):"))
    degree_angle = degrees(rad_angle)

    degree_angle = round(degree_angle, 2)
    print(degree_angle)









