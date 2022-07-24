# Q1-write a program to convert kilometers into miles

def kms_to_miles():
    """ This function is used to kilometers into miles"""
    a = int(input("enter the value you want to convert into miles:"))
    b = a*0.62137119
    print (a,'kms converted into ',b ,'miles')

kms_to_miles()

#Q2-Write a python program to convert Celsius into Fahrenheit

def C_to_F():
    '''This function is used to convert celsius into fahrenheit'''
    C = int(input('enter temperature in celsius:'))
    F = (C * (9/5)) + 32
    print(C,"degree celsius converted into",F,"into Fahrenheit")

C_to_F()

#Q3-Write a python program to display calendar

import calendar
year = int(input('enter the calendar year:'))
month = int(input('enter the month of calendar:'))
print(calendar.calendar(year))
print(calendar.month(year,month))

#Q4-Write a python program to solve quadratic equation
import math
def roots(a,b,c):
    '''This function is used for finding the roots of quadratic equation in the form of ax^2+bx+c'''
    d = b*b-4*a*c
    sqrt_d = math.sqrt(abs(d))
    if a ==0:
        print("Please enter correct quadratic equation")
    else:
        if d == 0:
            root_1 = ((-1) * b) / 2
            root_2 = ((-1) * b) / 2
            print("roots are real and equal", root_1, root_2)
        elif d > 0:
            root_1 = (((-1) * b) + sqrt_d) / (2 * a)
            root_2 = (((-1) * b) - sqrt_d) / (2 * a)
            print("Roots are real and unequal", root_1, root_2)
        else:
            root_1 = (- b / (2 * a), ' + i', sqrt_d/(2*a))
            root_2 = (- b / (2 * a), ' - i', sqrt_d/(2*a))
            print("Roots are complex", root_1, root_2)

roots(0,2,3)


#Q5-write a program to swap two variables without using temp
def swap():
     '''this function is used to swap values hold by two variables'''
     a = input("enter the value of first variable : ")
     b = input("enter the value of second variable : ")
     a ,b = b ,a
     print("value of first  and second variable after swapping" ,a,b)

swap()




