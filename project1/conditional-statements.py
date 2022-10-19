# # var1 = 5d
#
# # If else
#
# grade = input("What was your grade? ")
# if grade == "A":
#     print(f"your grade is: {5.0}")
# elif grade == "B":
#     print(f"your grade is: {4.0}")
# elif grade == "C":
#     print(f"your grade is: {3.0}")
# elif grade == "D":
#     print(f"your grade is: {2.0}")
# elif grade == "F":
#     print(f"your grade is: {1.0}")
# else:
#     print("You failed")
#
#
# #While Loop
#
# var1 = 7
# while var1 < 20:
#
#     print(f"This is var1: {var1}")
#     if var1%3 == 0:
#         break
#     var1 += 2

# #For Loop
# var1 = [1, 2, 3, 4, 5, 6, 7]
# for i in var1:
#     print(f"This is i: {i}")
#     if i == 5:
#         break

# for i in range(0, 101, 5):
#     print(f"This is i: {i}")


#Functions
# def wise():
#     new = 7
#     print(new+12)
#     print("I am wisdom")

# def wise(weight, height):
#     bmi = (height ** 2 )/weight
#     # print(bmi)
# # wise(60, 17)
#     return bmi
# w = int(input("Weight:"))
# h = int(input("Height:"))
#
# my_bmi = wise(w, h)
# print(my_bmi)

def BMI(weight=12, height=15):
    return (height**2)/weight

var2 = BMI()
print(var2)
