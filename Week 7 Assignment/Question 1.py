''' A Lower triangular matrix is a square matrix (where the number of rows and columns are equal)  where all the elements above the 
diagonal are zero.
For example, the following is an upper triangular matrix with the number of rows and columns equal to 3.

1 0 0
4 5 0
7 8 9

Write a program to convert a square matrix into a lower triangular matrix.

Input Format:
The first line of the input contains an integer number n which represents the number of rows and the number of columns.
From the second line, take n lines input with each line containing n integer elements. Elements are separated by space.

Output format:
Print the elements of the matrix with each row in a new line and each element separated by a space.'''

#CODE
a=[]
mat=[]
n=int(input())
# taking the input from user
for i in range(n):
    x=input()
    a=x.split()
    mat.append(a)
    
# Checking whether to put 0 or not 
for i in range(n):
    for j in range(n):
        if i>=j and j!=n-1:
            print(int(mat[i][j]),end=' ')
        elif i>=j and j==n-1:
            print(int(mat[i][j]),end='')
        elif i<j and j!=n-1:
            print(0,end=' ')
        else:
            print(0,end='')
    if(i!=n-1):
        print()
