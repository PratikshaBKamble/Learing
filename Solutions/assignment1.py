# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t7Ec6VrF6yfWyHqCk43P_HlKeRoE4YvO
"""

#11.) Write a python Program to Add ,Multiply, Divide & Substract two numbers.

a=int(input("kindly enter 1st number"))
b=int(input("kindly enter 2nd number"))
add=a+b
mul=a*b
sub=a-b
div=a/b

print("Addition of two number is",add)
print("Product of two number is",mul)
print("Substraction of two number is",sub)
print("Division of two number is",div)

"""Here,we are giving two numbers as an input from user and performing four types of operations (i.e. addition,multiplication,substraction and division) with these user given numbers/input.after performing these operations we are simply displyaing its result into the screen."""

#12.) Python Program for simple interest
P = int(input("Enter Principle"))
N = int(input("Enter No of years"))
R = float(input("Enter Rate"))


SI = (P * N * R) / 100

print("Simple interest = " , SI)

"""Here,we are calculating simplete intrest in this way,we are asking users to enter principle(amount),time(no of years) and rate(rate of intrest) and with the help of simple intrest's formula we are generating its output and are showing its result on the screen."""

#13.) Python Program for compound interest
P = int(input("Enter Principle"))
N = int(input("Enter No of years"))
R = float(input("Enter Rate"))

CI = P * (pow((1+R/100),N))

print("Compound interest = " , CI)

"""Here,we are calculating compound intrest in this way,we are asking users to enter principle(amount),time(no of years) and rate(rate of intrest) and with the help of compound intrest's formula we are generating its output and are showing its result on the screen."""

#14.) Python Program to check Armstrong Number
num = int(input("Number"))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp //= 10


if num == sum:
        print(num, "Number is an Armstrong number")
else:
        print(num, "Number is not an Armstrong number")

"""An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371. Write a program to find all Armstrong number in the range of 0 and 999."""

'''
15.) Given an integer, x perform the following conditional actions:
#	If  x is odd, print Weird
# If x is even and in the inclusive range of 2 to 5, print Not Weird
# If x is even and in the inclusive range of 6 to 20, print Weird
#	If x is even and greater than 20, print Not Weird
'''

n=int(input("Please enter a number"))
if((n%2!=0)):
  print("Weird")
else:
  if(n>=2 and n<=5):
    print("Not Weird")
  elif(n>=6 and n<=20):
    print("Weird")
  elif(n>20):
    print("Not Weird")

#16.) Python Program for Program to find area of a circle
# Area of circle = Pi * r * r

pi=3.14
r=float(input("Enter value for radius"))
areaofcircle = pi * r * r
print("Area of circle : " ,areaofcircle)

#17.) Python program to check whether a number is Prime or not

num = int(input("Please enter number"))

if num > 1:
    for i in range (2,num):
        if (num%i)==0:
            print(num,"is not a prime no")
            break
    else:
            print(num,"is prime no")
else:
    print("Invalid input")

"""a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)."""

#19.) Python Program for Fibonacci numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
n=int(input("Enter value for n"))

print(a)
print(b)

if n<0:
    print("Invalid input")
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

"""a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc."""

#20.) Python Program for How to check if a given number is Fibonacci number?

#21.) Program to print ASCII Value of a character

a= str(input("Enter a character"))

print("ASCII value is:",ord(a))

#22.) Python Program for Sum of first n natural numbers
# Python Program - Find Sum of Natural Numbers

print("Enter '0' for exit.");
num = int(input("Upto which number ? "));
if num == 0:
    exit();
elif num < 1:
    print("Kindly try to enter a positive number..exiting..");
else:
    sum = 0;
    while num > 0:
    	sum += num;
    	num -= 1;
    print("Sum = ", sum);

#23.) Python Program for Program to find area of a Square
s = float(input("Enter value for side "))
area = s * s

print("Area of circle is : ",area)

#24.) Python program to find weather the string entered by user is “hello world” or not.
x=str(input("Enter name"))

if("Hello World"==x):
    print("True")
else:
    print("false")

#25.)Python program to print the table of the input number.
num = int(input("Enter a number"))
for i in range(1,11):
    table= num * i
    print(num,"*",i,"=",table)