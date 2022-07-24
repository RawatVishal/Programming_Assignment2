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

def roots():
    '''This function is used for finding the roots of quadratic equation in the form of ax^2+bx+c'''
    a = int(input("enter the component of x^2 :"))
    b = int(input("enter the component of x:"))
    c = int(input("enter the value of c:"))
    d = int(((b*b)-4*a*c)**(0.5))
    root1 = (((-1)*(b))+d)/2
    root2 = (((-1)*(b))-d)/2
    print("The roots of the quadratic equation are",root1,root2)


roots()

#Q5-



