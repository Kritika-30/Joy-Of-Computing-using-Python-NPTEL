'''With a given list L of integers, write a program to print this list L after removing all duplicate values with original order preserved.

Example:

If the input list is

12 24 35 24 88 120 155 88 120 155

Then the output should be

12 24 35 88 120 155

Explanation:
Third, seventh and ninth element of the list L has been removed because it was already present.

Input Format:
In one line take the elements of the list L with each element separated by a space.

Output Format:
Print the elements of the modified list in one line with each element separated by a space.
Example:

Input:
12 24 35 24

Output:
12 24 35 
'''

#CODE
list1=[int(i) for i in input().split(" ")]            #input elements in the list1 

list2=[]                                  
for i in range(len(list1)):                           # element after removing duplicates in list2
  if list1[i] not in list2:
    list2.append(list1[i])
for i in list2:
    print(i,end=" ")

