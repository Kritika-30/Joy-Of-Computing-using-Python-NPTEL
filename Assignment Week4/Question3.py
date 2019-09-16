''' A list is given and we need to sort by taking randomly any two index using randint and swap them. Now check if list is sorted or not.
Keep doing this till list become sorted.'''

from random import randint
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)                        

sorted = True

while(sorted):
    j = randint(0,n-1)                                 #selecting two index randomly
    i = randint(0,n-1)
    arr[i],arr[j] = arr[j],arr[i]                       # swapping them
    for k in range(0,n-1):                              #check if list is sorted
        if (arr[k] > arr[k+1]):                        
            sorted = False
    
    if(sorted):
        break
    else:
        sorted = True

for i in range(n):                                    #printing the sorted list
    if(i==n-1):
        print(arr[i])
    else:
        print(arr[i],end=" ")
