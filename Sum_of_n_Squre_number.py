"""Write a python program for sum of squares of first n natural numbers"""


n = int(input("Enter number:= "))
sum =0
for i in range(1,n+1):
    sum = sum +i*i
print(sum)