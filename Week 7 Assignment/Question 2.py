'''Given a square matrix of N rows and columns, find out whether it is symmetric or not.

Input Format:
The first line of the input contains an integer number n which represents the number of rows and the number of columns.
From the second line, take n lines input with each line containing n integer elements with each element separated by a space.

Output Format:
Print 'YES' if it is symmetric otherwise 'NO'

Example:

Input:
2
1 2
2 1

Output:
YES'''

#CODE
n=int(input())
a=[]
mat=[]
matrix=[]
flag=0
for i in range(n):
  x=input()
  a=x.split()
  mat.append(a)
  
for i in range(n):
  for j in range(n):
    x=int(mat[i][j])          #checking the condition of symmetric
    y=int(mat[j][i])
    if x!=y:
      flag=1
      break
  
if flag==0:
  print('YES',end='')
else:
  print('NO',end='')
