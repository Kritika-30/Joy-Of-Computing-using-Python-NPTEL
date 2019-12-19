'''Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.

Input Format:

Sentence S in a single line

Output Format:
Print S after removing consecutive vowels

Example:
Input:
your article is in queue

Output:
yor article is in qu

Explanation:
In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed. In the fifth word, 'u', 'e', 'u' and 'e'
are appearing together, hence 'e', 'u', 'e' are removed.
'''

list1=['a','e','i','o','u']
s=input()
print(s[0],end='')
for i in range(1,len(s)):
  if (s[i-1] not in list1) or (s[i] not in list1):
    print(s[i],end="") 
