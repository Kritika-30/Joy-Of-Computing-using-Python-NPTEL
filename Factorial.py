# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:51:39 2019

@author: Kritika Singhal
"""
# Note: Both the method are used only for understanding. Both are doing same work.

# Iteration Method
def fact_iter(n):             
    f=1;
    for i in range(1,n+1):
        f=f*i;
    return f

# Recursion Method
def fact_rec(n):
    if n==0:
        return 1
    else:
        return n*fact_rec(n-1)
    

n=int(input('Enter a number '))                                     # Input of number in 'n'
print('Enter the way you want to calculate fact by recursion or by iteration ')
m=int(input('Enter choice 1:Recursion 2:Iteration '))                # Input of choice in m
if m==1:
    f=fact_rec(n)
    print('Factorial of '+ str(n) + ':'+ str(f))                 # calling recursion method  
else:
    f=fact_iter(n)
    print('Factorial of ' + str(n) +':'+ str(f))                 # calling iteration method 
