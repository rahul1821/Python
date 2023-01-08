"""Write a python program for nth
multiple of a number is Fibonacci series"""



def find(k, n):
   f1 = 0
   f2 = 1
   i =2;
   while i!=0:
      f3 = f1 + f2;
      f1 = f2;
      f2 = f3;
      if f2%k == 0:
         return n*i
      i+=1
   return
n = int(input("Enter first number:= "))
k = int(input("Enter second number:= "))
print(find(k,n));