"""Write a python program to find sum of square of digits of a given number."""


num = int(input("Enter Number: "))
temp = num
sum = 0
while temp != 0:
    rem = temp % 10
    sqr = rem * rem
    sum = sum + sqr
    temp = int(temp / 10)
print("Sum of squares of digits of", num, "=", sum)
