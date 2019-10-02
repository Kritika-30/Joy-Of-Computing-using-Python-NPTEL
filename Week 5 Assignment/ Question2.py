'''Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number
of moves required to sort the list using this method in ascending order. 

Input Format:
The first line of the input contains N distinct integers of list A separated by a space.

Output Format
Print the minimum number of moves required to sort the elements.'''


#!/usr/bin/python3
arr=[int(arr) for arr in input().split()]
n=len(arr)
arr1=sorted(arr)
f=0
for i in range(n):
  if arr[i]==arr1[f]:
  	f=f+1
print(n-f,end="")
