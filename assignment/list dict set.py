#Lists
#Q1. Create a list with the elements: 10, 20, 30.
l1=[10,20,30]
#Q2. Add the element 40 to the list created in the previous question.
l1.append(40)
print(l1)
#Q3. Access the second element of the list.
print(l1[1])
#Q4. Create a variable total that stores the sum of the first and second elements of the list.
print(l1[0]+l1[1])
#Q5. What is the length of the list?
print(len(l1))


#Sets:
#Create two sets, set1 and set2, with some common elements. Perform the following operations:
s1={1,2,3,8,5}
s2={2,4,5,8,7,6}
#Find the union of the sets.
print(s1|s2)
#Find the intersection of the sets.
print(s1.intersection(s2))
#Add a new element to set1.
s1.add(9)
print(s1)
#Print the modified sets.


#Dictionaries:
#Create a dictionary named student with keys 'name', 'age', and 'grade'. Assign corresponding values. Perform the following operations:
d1={'name':'vishnu','age':28,'grade':'A'}
print(d1)
#Add a new key 'subject' with the value 'math'.
d1['subject']='math'
print(d1)
#Update the 'grade' to 'B'.
d1.update({'grade':'B'})
print(d1)
#Print the final dictionary.
print(d1)
