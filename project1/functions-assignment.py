import math

# print("Yalloo!")
#
# print("We are trying to calculate the volume of a cone""\n The volume of a cone is πr2h/3")
#
#
# def coneVolume():
#     h = float(input("Input your value for height"))
#     r = float(input("Input your value for radius"))
#     π = 3.142
#
#     vol = (π * (r ** 2) * h) / 3
#
#
#     print("The volume of the cone is %.2f"%vol)
# coneVolume()
#
# print("We are going to calculate the time in seconds")
# def timeinSeconds():
#     years=int(input("What is your time in years"))
#     sec = years* 31556952
#     print("The time in seconds is %d"%sec,"seconds")
#
#
# timeinSeconds()
import cmath

print("The Quadratic formula""\n The Quadratic formula is (-b±√(b²-4ac))/(2a)")

def quadraticFormula():
    a=float(input("What is your value for 'a'"))
    b=float(input("What is your value for 'b'"))
    c=float(input("What is your value for 'c'"))

    discriminant= (b**2) - (4*a*c)
    if discriminant >0:
        x = -b
        y = (b ** 2) - (4 * a * c)
        z = math.sqrt(y)

        quad1 = (x + z) / 2 * a
        quad2 = (x - z) / 2 * a
        print("The first root is %d" % quad1)
        print("The second root is %d" % quad2)
    elif discriminant==0:
        x = -b
        y = (b ** 2) - (4 * a * c)
        z = math.sqrt(y)

        quad1 = (x + z) / 2 * a
        print("The roots are %d"%quad1)
    elif discriminant<0:
        x = -b
        y = (b ** 2) - (4 * a * c)
        z = cmath.sqrt(y)

        quad1 = (x + z) / 2 * a
        quad2 = (x - z) / 2 * a
        print(f"The first root is  {quad1}")
        print("The second root is {}".format(quad2))
quadraticFormula()
