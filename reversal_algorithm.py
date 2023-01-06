"""Write a python program for reversal algorithm for array rotation."""

array = []
# number of elements as input
size_of_array = int(input("Size of Array:=  "))

# iterating till the range
for i in range(0, size_of_array):
    elements_of_array = int(input(f"Enter element of {i} := "))
    array.append(elements_of_array)  # adding the element

n = int(input("Enter Number to rotate array:= "))

def rverseArray(array, start, end):
    while (start < end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end = end - 1


# Function to left rotate arr[] of size n by d
def leftRotate(array, d):
    n = len(array)
    rverseArray(array, 0, d - 1)
    rverseArray(array, d, n - 1)
    rverseArray(array, 0, n - 1)


# Function to print an array
def printArray(array):
    for i in range(0, len(array)):
        print("Rotated Array:= ", array)
        break


# Driver function to test above functions
leftRotate(array, n)  # Rotate array by 2
printArray(array)