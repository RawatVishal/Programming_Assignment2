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

#Q4-write a python program to check a prime number

b = int(input("enter the number : "))

if b > 1:
    for i in range(2,int(b/2)+1):
        if (b % i ) == 0:
            print(b,"is not a prime number")
            break
    else:
        print(b,"is a prime number")
else:
    print(b,"is not a prime number")

#Q5-Write a program to write prime number in interval of 1,10000

a = 1
b = 10001
for x in range(1,10001):
    if x==1:
        print("1 is not a prime number")
    elif x>1:
        for i in range(2,int(x//2)+1):
            if (x%i==0):
                pass
            else:
                print(x)
