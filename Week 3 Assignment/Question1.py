#Given a list of numbers (integers), find second maximum and second minimum in this list

input_string=input()                   #taking input from user in string format
list1=input_string.split()             #splitting the string to get separate numbers
for i in range(0,len(list1)):         
    list1[i]=int(list1[i])             #converting it to integer 

list1.sort()                              #sorting the numbers 
    
print(list1[len(list1)-2],end=" ")
print(list1[1])
