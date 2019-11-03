''' 
A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
The quick brown fox jumps over the lazy dog

Output:
YES
'''

#CODE
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input()
s=s.lower()
s=s.translate({ord(' '): None})
list2=list(s)      #converting string s into list
for i in list1:
  if (i in list2):
    flag=0
  else:
    flag=1
    break
if flag==1:
    print("NO",end='')
else:
    print("YES",end='')
  
