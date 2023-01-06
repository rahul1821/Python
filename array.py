"""Write a python for find reminder
of array multiplication divided by n."""
################################################

from functools import reduce
array = []
# number of elements as input
size_of_array = int(input("Size of Array:=  "))

# iterating till the range
for i in range(0, size_of_array):
    elements_of_array = int(input(f"Enter element of {i} := "))
    array.append(elements_of_array)  # adding the element

dividor = int(input("Enter Dividor number:= "))

def find_remainder(array, n):
    sum_1 = reduce(lambda x, y: x*y, array)
    remainder = sum_1 % n
    print("Remainder:= ",remainder)

find_remainder(array, dividor)
