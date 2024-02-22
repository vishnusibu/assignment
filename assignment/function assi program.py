#Assignment Programs in Function Concept
#1) Write a Python function to find the Max of three numbers
'''
l1=[8,55,64]
def maxi(x):
    print(max(x))
maxi(l1)
# or
def max():
    l1.sort()
    print(l1[-1])
max()
#2) Write a Python function to sum all the numbers in a list.
l2=[4,5,77,8,1,65,24,85]
def sum1(x):
    print(sum(x))
sum1(l2)
#or

def sumpy(y):
    ll=0
    for i in l2:
        ll=ll+i
    print(ll)
        
sumpy(l2)

#3) Write a Python function that accepts a string and calculate
#   the number of upper case letters and lower case letters.
l3='mahaVHI'

def vish(h):
    a=0
    b=0
    for i in h:
        if i.isupper():
            a+=1
        else:
            b+=1
    print('upper case number=',a)
    print('lower case number=',b)
vish(l3)
#4) Write a Python function to calculate the factorial of a number.
l4=int(input('factorial number=',))
def maha():
    a=1
    for i in range(1,l4+1):
        a*=i
    print(a)
maha()

#5) Write a Python function to check whether a given number is prime
l5=int(input())
def maha():
    if l5>1:
        for i in range(2,l5):
            if l5%i==0:
                print('it is not prime number')
                break
        else:
            print('it is prime namber')
    else:
        print('it is not prime number')
    
maha()

#6) Write a Python function to reverse a string.
l6='mahavishnu'
def maha(x):
    print(x[::-1])
maha(l6)

#7) Write a Python function to find the sum of all elements in a list.
l7=[1,5,74,6,8,2,45,62]
def samy(x):
    a=0
    for i in x:
        a+=i
    print(a)
samy(l7)        

#8) Write a Python function to count the number of vowels in a string
l8='sibu vish aeiou aeiou aeiou'
vow='a','e','i','o','u'
def maha(x):
    a=0
    for i in x:
        if i in vow:
            a=a+1
    print(a)
maha(l8)
'''
#9) Write a function that takes in a list of numbers and returns
#   the sum of all the even numbers in the list.
l9=[11,22,33,44,55,66,77,88,99]
def name(x):
    a=0
    for i in x:
        if i%2==0:
            a+=i
    print(a)
name(l9)
#10) Write a function that takes in a string and returns a new
#    string with all vowels removed.

l10='mahavishnu'
vow='a','e','i','o','u'
def name(l10):
    for i in l10:
        if i not in vow:
            print(i,end='') 
            
name(l10)


#11) Write a function that takes in a list of strings and returns
#    a new list with all strings that have more than 5 characters.
l11=('vishnu','sibu','mathi','sankari','mahavishnu')
def maha(x):
    for i in x:
        a=len(i)
        if a>5:
            print(i,end=' ')
maha(l11)










