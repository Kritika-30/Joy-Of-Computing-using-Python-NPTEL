#Given an integer number n, you have to print the factorial of this number

k = int(input())

fac = 1
for i in range(1,k+1):
    if(k==0):
        break
    fac=fac*i

print(fac)
