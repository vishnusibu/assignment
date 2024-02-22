#1. Write a Python function to find the maximum of three numbers.
l1=[4,25,5]
def name(l1):
    return max(l1)
print(name(l1))

#2. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
l2=[8, 2, 3, 0, 7]
def name(l2):
    return sum(l2)
print(name(l2))

#3. Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336
l3=[8, 2, 3, -1, 7]
def name(a,b,c,d,e):
    return(a*b*c*d*e)
print(name(8,2,3,-1,7))
#4. Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
l4="1234abcd"
def name(l4):
    return (l4[::-1])
name(l4)
#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
l5=int(input())
l=1
for i in range(1,l5+1):
        l=l*i
print(l,end='')
    

        
