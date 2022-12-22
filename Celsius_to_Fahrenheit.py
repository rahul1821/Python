"""Write a python program to convert temperature to and from Celsius to Fahrenheit."""

temp = float(input("Enter Temperature in Celsius: "))
# F = (°C × 9/5) + 32
fahrenheit = (temp*9/5)+32;
print("Celsius to Fahrenheit Temperature: %.2f" %fahrenheit)