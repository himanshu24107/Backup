import math

pi = 22/7
#first Set of code, meant to be runned
com = input("Type\" ? \" for details")

def command():
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
degtorad - Degrees to Radian
radtodeg - Radian to Degrees
pow - Power 
quad - Find Quadrant of an angle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
        ''')

if com =="?":
    command()

x = input("Enter your command:")



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
        if angle == -90:
            print("On Y(+ve) axis")
        elif angle ==-180:
            print("On X(-ve) axis")
        elif angle == -270:
            print("On Y(-ve) axis")
        elif angle == -360 or 0:
            print("On X(+ve) axis")
        else:    
            alpha = (angle//-90)+5
            print("Quadrant:", alpha)
    elif angle>360:
            alpha = (angle//90)-4
            print("Quadrant:", alpha)


def ratiotodeg():
    rad_angle = int(input("Enter to convert to trigo ratio(deg):"))
    degree_angle = math.degrees(rad_angle)

    degree_angle = round(degree_angle, 2)
    print(degree_angle)








#Here all command refer to function
if x=="degtorad":
    print('''
    +--------------------------------------------+
    | Welcome to Deg to Rad Measurent Calculator |
    +--------------------------------------------+
    ''')
    degtorad()

elif x=="radtodeg":
    print('''
    +--------------------------------------------+
    | Welcome to Rad to Deg Measurent Calculator |
    +--------------------------------------------+
    ''')
    radtodeg()
#Can add more Commands here!
elif x=="quad":
    print('''
    +----------------------------------+
    | Quadrant in which Angle Belongs! | 
    +----------------------------------+
    ''')
    quad()
    


else:
    print("Invalid command!")
    retry = input("Retry? Y/N")

    if retry == "Y" or "y":
        command()
    else:
        print('''
         +-------+   |     '
         |       |   |   '
         |       |   | '
         |       |   |-
         |       |   | '
         |       |   |   '
         +-------+   |     '   SEE YOU LATER:)
                           
        ''')






feed = input("Enjoyed! Want to try once again? Y/N")
if feed == "Y" or "y":
    command()

else:
    print('''
         +-------+   |     '
         |       |   |   '
         |       |   | '
         |       |   |-
         |       |   | '
         |       |   |   '
         +-------+   |     '
                           
        ''')