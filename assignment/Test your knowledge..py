'''
#Numbers
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

print(10*10/1+10-9.75)


#Answer these 3 questions without typing code. Then type code to check your answer.
  #What is the value of the expression 4 * (6 + 5)
a=int(input())
b=int(input())
c=int(input())
print(a*(b+c))
#ans=44
#What is the value of the expression 4 * 6 + 5
print(a*b+c)
#ans=29
#What is the value of the expression 4 + 6 * 5
print(a+b*c)
#ans=34

#What is the type of the result of the expression 3 + 1.5 + 4?
a1=3
b1=1.5
c1=4
print(a1+b1+c1)
#ans=8.5
#What would you use to find a number’s square root, as well as its square?
#square root
print(30**(1/2))
#square
print(30**2)

#Strings
#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
    
s1='hello'
print(s1[1])
#Reverse the string 'hello' using slicing:
print(s1[::-1])
#Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1:
print(s1[4])
# Method 2:
print(s1[-1])


#Lists
#Build this list [0,0,0] two separate ways.

# Method 1:
l1=[0]*3
print(l1)
# Method 2:
l2=[]
l2.append(0)
l2.append(0)
l2.append(0)
print(l2)
'''
#Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]
l3=list3[2]
l3[l3.index('hello')]='goodbye'
print(list3)

#Sort the list below:
list4 = [5,3,4,6,1]

print('list below',min(list4))

















