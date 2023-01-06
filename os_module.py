"""Write a python program to open a file
and check what are the access permissions
acquired by that file using os module?"""

import os
import sys

path1 = os.access("Rahul.txt", os.F_OK) # os.F_OK means file can Exists of this path
print("Exists the path:", path1)

# Checking access with os.R_OK
path2 = os.access("Rahul.txt", os.R_OK)#os.R_OK means file can Read
print("Access to read the file:", path2)

# Checking access with os.W_OK
path3 = os.access("Rahul.txt", os.W_OK) # os.W_OK means file can write.
print("Access to write the file:", path3)

# Checking access with os.X_OK
path4 = os.access("Rahul.txt", os.X_OK) # os.X_OK means file can execute.
print("Check if path can be executed:", path4)