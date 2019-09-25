#function to search an element
def binary_search(input_list,x,start,end):
    
   if(end>start):
       #calculate index of mid value
       mid=int((start+end)/2)
            
       #if element x found
       if(x==input_list[mid]):
           return mid
    
       # if element x is less than mid value of list 
       elif(x<input_list[mid]):
           return binary_search(input_list,x,start,mid-1)
      
       # if element x is greater than mid value of list 
       elif(x>input_list[mid]):
           return binary_search(input_list,x,mid+1,end)
        
   return -1
        
        
    
    
string=input('Enter the list of element in sorted order')
input_list=string.split()
for i in range(len(input_list)):
    input_list[i]=int(input_list[i])
    
x=int(input('Enter the element to search'))

#calling the binary_search function
value=binary_search(input_list,x,0,len(input_list))
if value==-1:
    print("Element not found")
else:
    # index is starting from 0 
    print("Element ",x," found at " , value)
