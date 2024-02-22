#Q1. Calculate the sum of all numbers from 1 to a given number
#Write a program to accept a number from a user and calculate
#the sum of all numbers from 1 to a given number

'''number=int(input('enter number :'))
s=0
for i in range(1,number+1):
    s+=i
print(s)


#Q2. Display numbers from -10 to -1 using for loop

a=-10
b=0
for i in range(a,b):
    print(i)


#Q3. Display Fibonacci series up to 10 terms The Fibonacci Sequence is a series
# of numbers. The next number is found by adding up the two numbers before it.
#The first two numbers are 0 and 1.

a=0
b=1
c=int(input())
d=0
for i in range(2,c+1):
    
    d=a+b
    a=b
    b=d
    print(d,end='')


#sum of all numbers from 1 to given n:
a=[]
for i in range(1,11):
    a.append(i)
print(a)
print(sum(a))
     #(or)
a=[]
for i in range(1,11):
    a.append(i)
c=0
for i in a:  
    c+=i
print(c)

#Q4. Find the factorial of a given number
#Write a program to use the loop to find the factorial of a given number.
c=5
tem=1
for i in range(1,c+1):
    tem*=i
print(tem)

#Q5. Reverse a given integer number
a=37231
a=str(a)
print(a[::-1])

a=1033458
for i in str(a)[::-1]:
    print(i,end='')

#Python program to check if the given string is a palindrome
a='dad'
if a==a[::-1]:
    print('palindrom')
else:
    print('not palindrom')
#Python program to get the Fibonacci series between 0 to 50.    

a=0
b=1
c=50
d=0
for i in range(2,c+1):
    d=a+b
    a=b
    b=d
    print(d,end='')'''

#Q6. Calculate the cube of all numbers from 1 to a given number
#Write a program to rint the cube of all numbers from 1 to a given number

l1=int(input('input number='))
for i in range(1,l1+1):
    print('Current Number is :',i,' and the cube is',i**3)




