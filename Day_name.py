"""Write a python Program to read a number and display corresponding day using if_elif_else."""

# day starting with, day 1 is Monday
day_number = int(input("Enter number 1 to 7: "))
if(day_number==1):
    print("Monday")
elif(day_number==2):
    print("Tuesday")
elif(day_number==3):
    print("Wednesday")
elif (day_number == 4):
    print("Truesday")
elif (day_number == 5):
    print("Friday")
elif(day_number==6):
    print("Satarday")
else:
    print("Sunday")