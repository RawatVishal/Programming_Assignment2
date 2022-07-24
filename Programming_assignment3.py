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