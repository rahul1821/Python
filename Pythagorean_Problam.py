"""Write a python program to that accepts length of three sides of a
 triangle as inputs. The program should indicate whether or not the triangle
 is a rightangled triangle (use Pythagorean theorem)."""

base = int(input("Enter Base: "))
hight = int(input("Enter Hight: "))
hypotenuse = int(input("Enter Hypotenuse: "))


# Pythagorean formula
# (hypotenuse)^2 = (base)^2 + (hight)^2

if((hypotenuse*hypotenuse) == (base*base) + (hight*hight)):
    print("It is Right angled triangle.")
else:
    print("It's not a Right angled triangle.")

