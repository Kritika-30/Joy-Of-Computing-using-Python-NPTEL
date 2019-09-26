# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:04:51 2019

@author: Kritika Singhal
"""

#function to find fibonacci till n
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    

# taking input from user
n=int(input('Enter the input'))
#calling the function
fb_num=fib(n)
#printing the return value i.e. fibonacci value
print(fb_num)

''' Note: Remember fibonacci starts from index 0 i.e. fib[0]=0, fib[1]=1....so on'''
