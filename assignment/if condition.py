'''Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:

Mark        Grade
>90          A
80 to 90     B
60 to 79     C
below 60     D

mark=int(input('enter the mark= '))
if mark>90:
    print('grade A')
elif mark>=80 and mark<=90:
    print('grade B')
elif mark>=60 and mark<=79:
    print('grade C')
elif mark>60:
    print('grade D')

#Q2 . Write a Python program that checks whether a given number is divisible by both 3 and 5.
#If it is, print "Divisible by both 3 and 5." Otherwise, print "Not divisible by both 3 and 5."
a=3
b=5
c=int(input())
if a%3==0 and b%5==0:
   print('Divisible by both 3 and 5')
else:
    print('Not divisible by both 3 and 5')'''

#Q3 . Write a Python program to check if a character entered by the user is a vowel or a consonant.

a=input('enter the character')
vowels=['a','e','i','o','u']
if a in vowels:
   print('character of vowels')
else:
   print('character not vowels')
#Q4 . Create a Python program that checks if a given number is even or odd.
#    Print "Even" if it's even, and "Odd" otherwise.
a=int(input())
if a%2==0:
   print('even')
else:
   print('odd')
#Q5 . Write a Python program to determine whether a year is a leap year.
#   A leap year is either divisible by 4 but not by 100, or divisible by 400.
