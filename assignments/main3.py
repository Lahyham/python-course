print("""====================================================
         ========================Welcome=====================
         This code is to calculate using the Quadratic Formula
         =====================================================""")

import cmath
a = float(input("Please input the value of a: "))
b = float(input("Please input the value of b: "))
c = float(input("Please input the value of c: "))

y = (b**2) - (4 * a * c)
min = ((-b -cmath.sqrt(y))/(2*a))
plus = ((-b +cmath.sqrt(y))/(2*a))

print(min , plus)