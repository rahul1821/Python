""""Write a program to read 3 subject marks
and display pass or failed using class and object."""

class mark:
    def grade(self, a, b, c):
        total = a + b + c
        per = total / 3
        if (per >= 50):
            print("Pass")
        else:
            print("Fail")


student = mark()
a = int(input())
b = int(input())
c = int(input())
student.grade(a, b, c)
