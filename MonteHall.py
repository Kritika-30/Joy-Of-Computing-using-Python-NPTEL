# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:20:28 2019

@author: Kritika Singhal
"""


import random 

doors=[0]*3
goatdoor=[0]*2
swap=0                 # num of swap
dont_swap=0            # num of dont swap
x=random.randint(0,2)  # x randomly chooses a door which has prize
doors[x]='BMW'  # prize i.e. BMW
j=0
while j<10:# running it for 10 times
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i]='Goat'
            goatdoor.append(i)
    choice=int(input('Enter your choice of door you want to open 0-1-2 '))
    
    #the door with goat is open 
    door_open=random.choice(goatdoor)
    # but it should not be same as choice of player
    while(door_open==choice):
        door_open=random.choice(goatdoor)
        
    ch=input('Do you want to swap y/n ')
    if ch=='y':
        if (doors[choice]=='Goat'):
            print('Player wins')
            swap=swap+1
        else:
            print('Player lost')
    else:
        if doors[choice]=='Goat':
            print('Player lost')
            dont_swap=dont_swap+1
        else:
            print('Player wins')
    j=j + 1    

print(swap)
print(dont_swap)
