"""Write a program to accept a string and
print the number of uppercase, lowercase, vowels,
consonants and spaces in the given string using Class"""



upper_case = input()

class upper:
        count =0

        for i in upper_case:
            if(i.isupper() == True):
                count +=1
class lower:
    count =0
    for i in upper_case:
        if(i.islower()==True):
            count +=1
class space:
    count =0
    for i in upper_case:
        if (i.isspace()==True):
            count +=1
class vowel:
    # vowels = "AaEeIiOoUu"
    final = [each for each in upper_case if each in "AaEeIiOoUu"]
    print("Vowels:= ", len(final))

class consonants:
    # vowels = "AaEeIiOoUu"
    final = [each for each in upper_case if each in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"]
    print("consonants:= ", len(final))



alphaa = upper()
lower1 = lower()
space1 = space()
vowel1 = vowel()
consonants1 = consonants()
print("Upper Case Letters:= ",alphaa.count)
print("Lower Case Letters:= ",lower1.count)
print("Space:= ",space1.count)