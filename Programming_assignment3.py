#Q1-Write a Python program to check if a number is Positive,Negative or zero

num = float(input("enter the value of number: "))
if num > 0:
    print(num," is a positive number")
elif num <0 :
    print(num ," is a negative number")
else:
    print("It is equal to zero ")

#Q2-Write a Python Program to check if a number is odd or even

a = float(input("enter the number : "))
if (a/2) == 0:
    print(a,"is an even number ")
else:
    print("It is a odd number ")

#Q3-Write  a program to check leap year


def leap_year():
    a = int(input("Enter the year: "))
    if (a % 400) == 0:
        print(a, "is a leap year")
    elif (a % 400) != 0:
        if (a % 4 == 0) and (a % 100 != 0) :
            print(a, "is a leap year")
    else:
        print("Entered year is not leap year ")

leap_year()

